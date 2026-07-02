import re

def extract_experience_from_jd(job_description):
    """
    Extract experience range like '5-9 years'
    """

    match = re.search(r'(\d+)\s*[-–]\s*(\d+)\s*years', job_description.lower())

    if match:
        return int(match.group(1)), int(match.group(2))

    return None, None


def experience_score(candidate_exp, min_exp, max_exp):

    if min_exp is None:
        return 1.0

    if min_exp <= candidate_exp <= max_exp:
        return 1.0

    if candidate_exp < min_exp:
        diff = min_exp - candidate_exp
    else:
        diff = candidate_exp - max_exp

    score = max(0, 1 - diff / 10)

    return round(score, 2)