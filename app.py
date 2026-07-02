import pandas as pd
import time
import json

from utils.jd_loader import load_job_description
from models.ranker import rank_candidates
# from utils.jsonl_loader import load_jsonl

with open("data/sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

# candidates = load_jsonl(
#     "data/candidates.jsonl"
# )



print(f"Total Candidates : {len(candidates)}")

job_description = load_job_description(
        "data/job_description.docx"
    )
start = time.time()

ranking = rank_candidates(
    job_description,
    candidates
)

end = time.time()

print(f"\nTime Taken : {end-start:.2f} seconds")


print("\nTOP 10 CANDIDATES\n")

for i, candidate in enumerate(ranking[:10], start=1):

    print("=" * 50)
    print(f"Rank : {i}")
    print(f"Candidate : {candidate['name']}")
    print(f"ID : {candidate['candidate_id']}")
    print(f"Final Score : {candidate['final_score']:.2f}")

    print(f"Semantic Score : {candidate['semantic_score']:.2f}")
    print(f"Skill Score : {candidate['skill_score']:.2f}")
    print(f"Experience Score : {candidate['experience_score']:.2f}")
    print(f"Behavior Score : {candidate['behavior_score']:.2f}")
    print(f"Intent Score : {candidate['intent_score']:.2f}")

    print("Matched Skills :", candidate["matched_skills"])
    print("Missing Skills :", candidate["missing_skills"])
    print("Reason :")
    print(candidate["reason"])

submission = []

for rank, candidate in enumerate(ranking[:100], start=1):

    submission.append({

        "rank": rank,

        "candidate_id": candidate["candidate_id"],

        "candidate_name": candidate["name"],

        "final_score": candidate["final_score"]

    })

df = pd.DataFrame(submission)

df.to_csv(
    "output/submission.csv",
    index=False
)

print("\nSubmission CSV Generated Successfully!")
