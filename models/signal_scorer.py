def signal_score(signals):
    score = 0

    # Open to work
    if signals["open_to_work_flag"]:
        score += 0.20

    # Verified profile
    if signals["verified_email"]:
        score += 0.05

    if signals["verified_phone"]:
        score += 0.05

    # Recruiter response
    score += min(signals["recruiter_response_rate"], 1.0) * 0.20

    # Interview completion
    score += signals["interview_completion_rate"] * 0.20

    # Offer acceptance
    score += signals["offer_acceptance_rate"] * 0.15

    # GitHub activity
    score += (signals["github_activity_score"] / 100) * 0.15

    return round(min(score, 1.0), 2)