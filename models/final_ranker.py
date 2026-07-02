def final_score(
    semantic,
    skills,
    experience,
    behavior,
    intent
):

    score = (
        semantic * 0.35 +
        skills * 0.25 +
        experience * 0.15 +
        behavior * 0.10 +
        intent * 0.15
    )

    return round(score * 100, 2)