def generate_reason(candidate):

    reasons = []

    if candidate["semantic_score"] >= 0.60:
        reasons.append(
            "Strong semantic match with the job description."
        )

    elif candidate["semantic_score"] >= 0.45:
        reasons.append(
            "Moderate semantic relevance."
        )

    if candidate["experience_score"] == 1:
        reasons.append(
            "Experience matches the required range."
        )

    if len(candidate["matched_skills"]) > 0:

        reasons.append(

            f"Matched {len(candidate['matched_skills'])} key skills."

        )

    if candidate["behavior_score"] >= 0.60:

        reasons.append(

            "Positive recruiter engagement."

        )

    if len(candidate["missing_skills"]) > 0:

        reasons.append(

            "Missing: " +

            ", ".join(candidate["missing_skills"][:3])

        )

    return " ".join(reasons)