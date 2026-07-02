from tqdm import tqdm

from utils.document_builder import build_candidate_document

from utils.cache_embeddings import (
    load_embeddings,
    save_embeddings
)

from models.semantic_ranker import (
    get_embedding,
    get_embeddings,
    similarity_score
)

from models.skill_matcher import (
    extract_skills_from_jd,
    skill_match_score
)

from models.experience_matcher import (
    extract_experience_from_jd,
    experience_score
)

from models.signal_scorer import signal_score
from models.intent_scorer import intent_score
from models.final_ranker import final_score
from models.explainer import generate_reason
from models.faiss_index import build_faiss_index

from models.semantic_ranker import search_top_k


def rank_candidates(job_description, candidates):

    # ---------------------------------
    # Extract JD Information
    # ---------------------------------

    jd_skills = extract_skills_from_jd(
        job_description
    )

    min_exp, max_exp = extract_experience_from_jd(
        job_description
    )

    # ---------------------------------
    # Build Candidate Documents
    # ---------------------------------

    print("Building candidate documents...")

    documents = [
        build_candidate_document(candidate)
        for candidate in candidates
    ]

    # ---------------------------------
    # JD Embedding
    # ---------------------------------

    print("Generating JD embedding...")

    jd_embedding = get_embedding(
        job_description
    )

    # ---------------------------------
    # Candidate Embeddings (Cached)
    # ---------------------------------

    candidate_embeddings = load_embeddings()

    if candidate_embeddings is None:

        print("Generating candidate embeddings...")

        candidate_embeddings = get_embeddings(
            documents
        )

        save_embeddings(
            candidate_embeddings
        )

    else:

        print("Loaded cached embeddings.")

    # ---------------------------------
    # Ranking
    # ---------------------------------

    results = []

    for candidate, embedding in tqdm(
        zip(candidates, candidate_embeddings),
        total=len(candidates),
        desc="Ranking Candidates"
    ):

        semantic = float(
            similarity_score(
                jd_embedding,
                embedding
            )
        )

        candidate_skills = [
            skill["name"]
            for skill in candidate["skills"]
        ]

        skills, matched_skills, missing_skills = skill_match_score(
            jd_skills,
            candidate_skills
        )

        experience = experience_score(
            candidate["profile"]["years_of_experience"],
            min_exp,
            max_exp
        )

        behavior = signal_score(
            candidate["redrob_signals"]
        )

        intent = intent_score(
            candidate
        )

        score = final_score(
            semantic,
            skills,
            experience,
            behavior,
            intent
        )

        candidate_result = {

            "candidate_id": candidate["candidate_id"],

            "name": candidate["profile"]["anonymized_name"],

            "semantic_score": semantic,

            "skill_score": skills,

            "experience_score": experience,

            "behavior_score": behavior,

            "intent_score": intent,

            "matched_skills": matched_skills,

            "missing_skills": missing_skills,

            "final_score": score
        }

        candidate_result["reason"] = generate_reason(
            candidate_result
        )

        results.append(
            candidate_result
        )

    # ---------------------------------
    # Sort Results
    # ---------------------------------

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return results
