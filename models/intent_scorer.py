def intent_score(candidate):

    profile = candidate["profile"]

    summary = profile["summary"].lower()

    title = profile["current_title"].lower()

    # Career titles
    career_titles = " ".join(
        [
            job["title"]
            for job in candidate["career_history"]
        ]
    ).lower()

    # Career descriptions
    career_descriptions = " ".join(
        [
            job["description"]
            for job in candidate["career_history"]
        ]
    ).lower()

    text = (
        summary
        + " "
        + title
        + " "
        + career_titles
        + " "
        + career_descriptions
    )

    score = 0

    keywords = {
    "ranking": 0.20,
    "retrieval": 0.20,
    "recommendation": 0.20,
    "search": 0.15,
    "embedding": 0.15,
    "vector": 0.10,
    "production": 0.10,
    "machine learning": 0.10,
    "ml": 0.05,
    "pipeline": 0.05,
    "feature engineering": 0.05,
    "inference": 0.10,
    "serving": 0.10
}

    score = 0

    for keyword, weight in keywords.items():
        if keyword in text:
            score += weight

    return min(score, 1.0)