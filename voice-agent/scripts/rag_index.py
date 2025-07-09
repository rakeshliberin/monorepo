# rag_index.py  – re‑build the multilingual vector index
import os
import re

import qdrant_client
from dotenv import load_dotenv
from google.genai.types import EmbedContentConfig
from llama_index.core import (
    Settings,
    StorageContext,
    VectorStoreIndex,
    SimpleDirectoryReader,
)
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.embeddings.google_genai.base import VertexAIConfig
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import models
from qdrant_client.http.models import (
    VectorParams,
    Distance,
    ScalarQuantizationConfig,
    ScalarType,
    ScalarQuantization,
    SparseIndexParams,
)
from torch import mode

load_dotenv(override=True)

COLLECTION = "igl_support_docs_optimized"
DOCS_DIR = "./docs/docs_opt"
BATCH_SIZE = 16  # safe & fast for Vertex

# ── 1. Multilingual embedding model ──────────────────────────────────────────
doc_embed = GoogleGenAIEmbedding(
    model_name="text-embedding-004",
    embed_batch_size=BATCH_SIZE,
    api_key=os.getenv("GOOGLE_API_KEY"),
    embedding_config=EmbedContentConfig(
        task_type="RETRIEVAL_QUERY",
        output_dimensionality=768,
    ),
    vertexai_config=None,
    # vertexai_config=VertexAIConfig(
    #     project=os.environ.get("GOOGLE_CLOUD_PROJECT"),
    #     location=os.environ.get("GOOGLE_CLOUD_LOCATION"),
    # ),
)

# doc_embed = HuggingFaceEmbedding(
#     model_name="Qwen/Qwen3-Embedding-0.6B",
#     embed_batch_size=BATCH_SIZE,
#     show_progress_bar=True,
# )

Settings.embed_model = doc_embed
Settings.chunk_size = 512
Settings.chunk_overlap = 64


# ── 2. Markdown loader that inlines synonyms before embedding ───────────────
class MultilingualMarkdownReader(SimpleDirectoryReader):
    SYM_RE = re.compile(r"<!--\s*synonyms:\s*(.*?)\s*-->")

    def _postprocess_nodes(self, nodes):
        for node in nodes:
            syns = self.SYM_RE.findall(node.text)
            if syns:
                node.text += "\n" + " ".join(
                    s.strip() for s in "|".join(syns).split("|")
                )
        return nodes


# docs = MultilingualMarkdownReader(DOCS_DIR, recursive=True).load_data(
#     show_progress=True
# )

docs = SimpleDirectoryReader(input_dir=DOCS_DIR).load_data(show_progress=True)

# ── 3. Qdrant collection (HNSW m16 + INT8 quantisation) ─────────────────────
qclient = qdrant_client.QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

qclient.delete_collection(COLLECTION)

if not qclient.collection_exists(COLLECTION):
    qclient.create_collection(
        COLLECTION,
        vectors_config={
            "igl-dense": VectorParams(
                size=768, distance=Distance.COSINE, on_disk=True  # 768 for this model
            )
        },
        quantization_config=ScalarQuantization(
            scalar=ScalarQuantizationConfig(type=ScalarType.INT8, always_ram=False)
        ),
        sparse_vectors_config={
            "igl-sparse": models.SparseVectorParams(
                index=SparseIndexParams(on_disk=True)
            )
        },
    )

vector_store = QdrantVectorStore(
    client=qclient,
    collection_name=COLLECTION,
    enable_hybrid=True,
    fastembed_sparse_model="Qdrant/bm25",
    batch_size=BATCH_SIZE,
    sparse_vector_name="igl-sparse",
    dense_vector_name="igl-dense",
)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# ── 4. Build & persist index ────────────────────────────────────────────────
index = VectorStoreIndex.from_documents(
    docs,
    storage_context=storage_context,
    show_progress=True,
)
index.storage_context.persist(persist_dir="./storage")
print("✅  Multilingual vector index built & persisted")
