from .nlp_utils import preprocess_text, calculate_text_similarity
from job.models import Job
from resume.models import Resume
class JobMatchEngine:
    def __init__(self):
        # self.job_database = job_database
        # self.candidate_database = candidate_database
        pass

    def match_jobs(request):
        """
        Match jobs to a candidate based on their skills.

        Args:
            candidate_name (str): Name of the candidate to match jobs for.

        Returns:
            list: List of tuples containing matched jobs and their similarity scores.
        """
        # candidate = self.candidate_database.find_candidate_by_name(candidate_name)
        # if not candidate:
        #     print(f"Candidate '{candidate_name}' not found in the database.")
        #     return []
        resume = Resume.objects.get(id=request.user.id)
        
        candidate_skills = preprocess_text(str(resume.skills))
        # print(Resume.objects.filter()[1:])
        job_matches = []
        # temp_jobs=[]
        for job in Job.objects.filter(is_available=True):
            job_skills = preprocess_text(str(job.skills))
            print(candidate_skills)
            print('This is job_skills')
            print(job_skills)
            # print(job_skills)
            similarity_score = calculate_text_similarity(" ".join(candidate_skills), " ".join(job_skills))
            # print(job,similarity_score)
            # print(job,similarity_score)
            job_matches.append((job, similarity_score))
            print(similarity_score)
            # print(job_matches)
            # temp_jobs.append(job)
        return sorted(job_matches, key=lambda x: x[1], reverse=True)
        return temp_jobs

    # def recommend_jobs(self, candidate_name, num_recommendations=5):
    #     """
    #     Recommend top jobs for a candidate based on their skills.

    #     Args:
    #         candidate_name (str): Name of the candidate.
    #         num_recommendations (int): Number of jobs to recommend.

    #     Returns:
    #         list: List of recommended job titles.
    #     """
    #     matched_jobs = self.match_jobs(candidate_name)
    #     recommended_jobs = [job[0].title for job in matched_jobs[:num_recommendations]]
    #     return recommended_jobs
