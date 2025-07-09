# import os
# import functools
# import asyncio
# import time
# from functools import lru_cache
# from llama_index.core import Settings, VectorStoreIndex
# from llama_index.vector_stores.qdrant import QdrantVectorStore
# from llama_index.core.retrievers import BaseRetriever
# from llama_index.core.vector_stores.types import VectorStoreQueryMode
# from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
# import qdrant_client
# from qdrant_client.http import models as qmodels
#
# # ---------- 1. Shared embeddings + model -------------------------------
# EMBED_MODEL = GoogleGenAIEmbedding(model="text-embedding-005", embed_batch_size=128)
# Settings.embed_model = EMBED_MODEL  # global config
#
# # ---------- 2. Build a tuned vector store ------------------------------
#
#
# async def _vector_store() -> QdrantVectorStore:
#     client = qdrant_client.AsyncQdrantClient(
#         url=os.getenv("QDRANT_URL"),
#         api_key=os.getenv("QDRANT_API_KEY"),
#     )
#
#     # Enable binary quantisation & HNSW params on the *collection*:
#     await client.update_collection(
#         collection_name=os.getenv("QDRANT_COLLECTION", "igl_support_docs"),
#         hnsw_config=qmodels.HnswConfigDiff(m=16, ef_construct=256),
#         optimizers_config=qmodels.OptimizersConfigDiff(default_segment_number=1),
#         quantization_config=qmodels.ScalarQuantization(
#             scalar=qmodels.ScalarQuantizationConfig(
#                 type=qmodels.ScalarType.INT8,
#                 quantile=0.99,
#                 always_ram=True,
#             ),
#         ),
#     )
#     return QdrantVectorStore(
#         aclient=client,
#         collection_name=os.getenv("QDRANT_COLLECTION", "igl_support_docs"),
#     )
#
#
# # ---------- 3. Factory to create a *per‑query* retriever ---------------
#
#
# async def build_retriever(
#     alpha: float = 0.6,
#     similarity_top_k: int = 3,
#     sparse_top_k: int = 3,
# ) -> BaseRetriever:
#     """
#     Hybrid (dense + BM25) retriever with tunable alpha and top‑k.
#     Call with different knobs depending on query length / difficulty.
#     """
#     vstore = await _vector_store()
#     index = VectorStoreIndex.from_vector_store(vstore)
#
#     retriever = index.as_retriever(
#         similarity_top_k=similarity_top_k,
#         sparse_top_k=sparse_top_k,
#         alpha=alpha,
#         mode=VectorStoreQueryMode.HYBRID,
#     )
#     return retriever
#
#
# # ---------- 4. Tiny in‑process cache for hot queries -------------------
# @lru_cache(maxsize=256)
# async def cached_retrieve(query: str, alpha: float, sim_k: int, sp_k: int):
#     retriever = await build_retriever(alpha, sim_k, sp_k)
#     # synchronous wrapper – LlamaIndex retrievers are async‑friendly
#     return await retriever.aretrieve(query)