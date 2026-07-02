def calculate_score(
    semantic,
    skill_score,
    experience_score,
    signal_score,
    bonus_score
):

    final_score = (
        semantic * 0.50 +
        skill_score * 0.20 +
        experience_score * 0.15 +
        signal_score * 0.10 +
        bonus_score * 0.05
    )

    return round(final_score * 100, 2) 