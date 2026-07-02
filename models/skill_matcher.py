import re

def extract_skills_from_jd(job_description):
    """
    Extracts skills from the Job Description.
    We'll improve this later using NLP.
    """

    common_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "LLM",
        "Embeddings",
        "Vector Database",
        "FAISS",
        "Milvus",
        "Pinecone",
        "LangChain",
        "PyTorch",
        "TensorFlow",
        "AWS",
        "Azure",
        "GCP",
        "Docker",
        "Kubernetes",
        "FastAPI",
        "Flask",
        "NLP",
        "RAG",
        "Retrieval",
        "Ranking"
    ]

    found = []

    jd_lower = job_description.lower()

    for skill in common_skills:
        if skill.lower() in jd_lower:
            found.append(skill)

    return found


def skill_match_score(jd_skills, candidate_skills):

    if len(jd_skills) == 0:
        return 0, [], []

    candidate_lower = [s.lower() for s in candidate_skills]

    matched = []
    missing = []

    for skill in jd_skills:

        if skill.lower() in candidate_lower:
            matched.append(skill)
        else:
            missing.append(skill)

    score = len(matched) / len(jd_skills)

    return score, matched, missing