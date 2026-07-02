import faiss
import numpy as np


def build_faiss_index(embeddings):

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(
        dimension
    )

    faiss.normalize_L2(
        embeddings
    )

    index.add(
        embeddings
    )

    return index