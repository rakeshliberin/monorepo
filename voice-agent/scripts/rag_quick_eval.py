# rag_quick_eval.py  – one‑file sanity + metrics
"""
Prereqs (same venv as main app):
    pip install llama-index-core qdrant-client rich langchain google-generativeai
"""

import asyncio
import os
import time

import qdrant_client
from dotenv import load_dotenv
from google.genai.types import EmbedContentConfig
from llama_index.core import Settings, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.embeddings.google_genai.base import VertexAIConfig
from llama_index.llms import google_genai
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client.http.models import (
    ScalarQuantization,
    ScalarQuantizationConfig,
    ScalarType,
)
from rich import print

# ─── ENV / CONFIG ────────────────────────────────────────────────────────────
load_dotenv()

COLLECTION = "igl_support_docs_optimized"
EVAL_PATH = os.getenv("EVAL_FILE", "./rag_eval_set.jsonl")  # 25‑Q set from earlier
TOP_K = 10
BATCH_SIZE = 16

EMBED_MODEL = GoogleGenAIEmbedding(
    model_name="text-embedding-004",
    embed_batch_size=BATCH_SIZE,
    embedding_config=EmbedContentConfig(task_type="RETRIEVAL_QUERY"),
    vertexai_config=None,
    # vertexai_config=VertexAIConfig(
    #     project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    #     location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    # ),
)
# EMBED_MODEL = HuggingFaceEmbedding(
#     model_name="Qwen/Qwen3-Embedding-0.6B",
#     embed_batch_size=BATCH_SIZE,
#     show_progress_bar=True,
# )
LLM_MODEL = GoogleGenAI(
    model="gemini-2.0-flash",
    temperature=0.2,
    vertexai_config=None,
    # vertexai_config=google_genai.base.VertexAIConfig(
    #     project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    #     location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    # ),
)

Settings.embed_model = EMBED_MODEL
Settings.llm = LLM_MODEL

# ─── Build retriever ----------------------------------------------------------
qclient = qdrant_client.QdrantClient(
    url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY")
)
aqclient = qdrant_client.AsyncQdrantClient(
    url=os.getenv("QDRANT_URL"), api_key=os.getenv("QDRANT_API_KEY")
)

vstore = QdrantVectorStore(
    client=qclient,
    aclient=aqclient,
    collection_name=COLLECTION,
    quantization_config=ScalarQuantization(
        scalar=ScalarQuantizationConfig(type=ScalarType.INT8, always_ram=False)
    ),
    enable_hybrid=True,
    fastembed_sparse_model="Qdrant/bm25",
    batch_size=BATCH_SIZE,
    sparse_vector_name="igl-sparse",
    dense_vector_name="igl-dense",
)
index = VectorStoreIndex.from_vector_store(vector_store=vstore)
async_retriever = index.as_retriever(
    similarity_top_k=4,
    sparse_top_k=8,
    vector_store_query_mode="hybrid",
)


# ─── Helpers ------------------------------------------------------------------
async def retrieve_ctx(question: str):
    """Top‑k retrieval → list of (content, metadata) dicts."""
    hits = await async_retriever.aretrieve(question)
    return [
        {
            "text": h.node.get_content(),
            "metadata": h.metadata,
        }
        for h in hits
    ]


def build_prompt(question: str, contexts):
    ctx_block = "\n\n---\n".join(
        f"[{c['metadata'].get('source','doc')}] {c['text']}" for c in contexts
    )
    return (
        "You are IGL customer‑support assistant. "
        "Answer the user's query ONLY from the context. "
        "If context is insufficient, say you do not have that information.\n\n"
        f"Context:\n{ctx_block}\n\nQuestion: {question}\nAnswer:"
    )


async def llm_complete(prompt: str):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, LLM_MODEL.complete, prompt)


async def llm_grade(question, context, answer):
    """
    Self‑grade via Gemini: returns True if answer satisfies ground‑truth.
    """
    grade_prompt = (
        "You are a strict evaluator for a Q&A system.\n"
        f"Question: {question}\n"
        f"Context:\n{context}\n"
        f"System answer:\n{answer}\n\n"
        "Respond ONLY 'CORRECT' or 'INCORRECT'."
    )
    verdict = (await llm_complete(grade_prompt)).text.strip().upper()
    return verdict.startswith("CORRECT")


def retrieval_hit(contexts, ground_truth):
    gt = ground_truth.lower()
    return any(gt[:80] in c["text"].lower() for c in contexts)  # very simple match


# ─── Evaluation loop ----------------------------------------------------------
async def run_eval():

    query = "I want to understand self-billing"
    answers = await retrieve_ctx(query)

    print(f"\n[bold cyan]Q:[/bold cyan] {query}")
    for ans in answers:
        print(f"\n[bold green]Context:[/bold green] \n {ans}")

    t0 = time.perf_counter()
    answer = (await llm_complete(build_prompt(query, answers))).text.strip()
    print(f"\n[bold green]A:[/bold green] \n {answer}")
    latency = time.perf_counter() - t0
    print(f"[yellow]latency:[/yellow] {latency*1000:.0f}ms")
    correct = await llm_grade(query, answers, answer)
    print(f"[yellow]LLM‑grade:[/yellow] {'✅' if correct else '❌'}")

    # items = [
    #     json.loads(l) for l in Path(EVAL_PATH).read_text(encoding="utf-8").splitlines()
    # ]
    # tot = len(items)
    # hit_ok = ans_ok = both_ok = 0
    # latencies = []
    #
    # for i, item in enumerate(items, 1):
    #     q, gt = item["question"], item["ground_truth"]
    #     print(f"\n[bold cyan]{i}. Q:[/bold cyan] {q}")
    #
    #     t0 = time.perf_counter()
    #     ctxs = await retrieve_ctx(q)
    #     answer = (await llm_complete(build_prompt(q, ctxs))).text.strip()
    #     latency = time.perf_counter() - t0
    #     latencies.append(latency)
    #
    #     hit = retrieval_hit(ctxs, gt)
    #     correct = await llm_grade(q, gt, answer)
    #     both = hit and correct
    #     hit_ok += hit
    #     ans_ok += correct
    #     both_ok += both
    #
    #     print(f"[bold green]A:[/bold green] {answer}")
    #     print(
    #         f"[yellow]retrieval‑hit:[/yellow] {'✅' if hit else '❌'}   "
    #         f"[yellow]LLM‑grade:[/yellow] {'✅' if correct else '❌'}   "
    #         f"[yellow]latency:[/yellow] {latency*1000:.0f}ms"
    #     )
    #
    # # Summary
    # print("\n[bold magenta]=== SUMMARY ===[/bold magenta]")
    # print(f"Total questions: {tot}")
    # print(f"Retrieval hit‑rate  (k={TOP_K}): {hit_ok/tot:.2%}")
    # print(f"Answer correctness (LLM):        {ans_ok/tot:.2%}")
    # print(f"Both retrieval+answer OK:        {both_ok/tot:.2%}")
    # print(f"Avg latency: {sum(latencies)/tot*1000:.0f}ms")


# ─── main ---------------------------------------------------------------------
if __name__ == "__main__":
    asyncio.run(run_eval())
