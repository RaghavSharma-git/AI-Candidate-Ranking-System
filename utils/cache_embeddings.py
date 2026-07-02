import pickle
import os

CACHE_FILE = "data/candidate_embeddings.pkl"


def load_embeddings():

    if os.path.exists(CACHE_FILE):

        with open(CACHE_FILE, "rb") as f:

            return pickle.load(f)

    return None


def save_embeddings(embeddings):

    with open(CACHE_FILE, "wb") as f:

        pickle.dump(
            embeddings,
            f
        )