def parse_candidate(candidate):
    profile = candidate["profile"]

    parsed = {
        "candidate_id": candidate["candidate_id"],
        "name": profile["anonymized_name"],
        "headline": profile["headline"],
        "summary": profile["summary"],
        "experience": profile["years_of_experience"],
        "location": profile["location"],
        "current_title": profile["current_title"],
        "current_company": profile["current_company"],

        "skills": [skill["name"] for skill in candidate["skills"]],

        "education": [
            edu["degree"] + " - " + edu["field_of_study"]
            for edu in candidate["education"]
        ],

        "career": [
            job["title"]
            for job in candidate["career_history"]
        ],

        "signals": candidate["redrob_signals"]
    }

    return parsed
