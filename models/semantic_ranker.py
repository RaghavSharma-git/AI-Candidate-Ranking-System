from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):
    """
    Generate embedding for a single text.
    """
    return model.encode(
        text,
        convert_to_numpy=True,
        normalize_embeddings=True
    )


def get_embeddings(texts):
    """
    Generate embeddings for multiple texts together (FAST).
    """
    return model.encode(
        texts,
        batch_size=64,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )


def similarity_score(embedding1, embedding2):
    return cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

import faiss
import numpy as np


def search_top_k(
    jd_embedding,
    index,
    k=500
):

    query = np.array(
        jd_embedding,
        dtype="float32"
    )

    faiss.normalize_L2(query)

    scores, ids = index.search(
        query,
        k
    )

    return scores[0], ids[0]