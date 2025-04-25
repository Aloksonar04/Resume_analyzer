def rank_resumes(resume_data, target_skills):
    def score(resume_skills):
        return sum(skill in resume_skills for skill in target_skills)

    ranked = sorted(resume_data, key=lambda x: score(x['skills']), reverse=True)
    return ranked
