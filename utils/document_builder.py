def build_candidate_document(candidate):
    
    profile = candidate["profile"]

    skills = ",".join(
        [skill["name"] for skill in candidate["skills"]]
    )
    
    education = ",".join(
        [
            f'{edu["degree"]} in {edu["field_of_study"]}'
            for edu in candidate["education"]
        ]
    )
    career = ",".join(
        [
            f'{job["title"]} at {job["company"]}'
            for job in candidate["career_history"]
        ]
    )

    document = f"""
    Name: {profile["anonymized_name"]}

    Headline:
    {profile["headline"]}

    Summary:
    {profile["summary"]}

    Experience:
    {profile["years_of_experience"]} years

    Current Role:
    {profile["current_title"]}

    Skills:
    {skills}

    Education:
    {education}

    Career History:
    {career}
"""

    return document

