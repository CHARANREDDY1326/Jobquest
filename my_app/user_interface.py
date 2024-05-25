from .job_match_engine import JobMatchEngine
from job.models import Job
class UserInterface:
    def __init__(self):
        # self.job_database = JobDatabase()
        # self.candidate_database = CandidateDatabase()
        # self.job_match_engine = JobMatchEngine(self.job_database, self.candidate_database)
        pass

    # def add_job(self, title, description, skills):
    #     """
    #     Add a new job to the system.

    #     Args:
    #         title (str): Title of the job.
    #         description (str): Description of the job.
    #         skills (str): Skills required for the job.
    #     """
    #     self.job_database.add_job(title, description, skills)
    def get_jobs(self):
            #for Available jobs
        # Retrieve all jobs (you can add filtering or ordering if needed)
            # return Job.objects.all()

            return Job.objects.filter(is_available=True),[job.title for job in Job.objects.filter()]
    # def add_candidate(self, name, skills):
    #     """
    #     Add a new candidate to the system.

    #     Args:
    #         name (str): Name of the candidate.
    #         skills (str): Skills possessed by the candidate.
    #     """
    #     self.candidate_database.add_candidate(name, skills)

    def match_candidates_to_jobs(self,request):
        from resume.models import Resume
        """
        Match candidates to available jobs and store the results.
        """

        results = JobMatchEngine.match_jobs(request)
        better_jobs = []
        for result in results:
                # print(f" - {job.title} (Similarity Score: {similarity_score})")

                if(result[1] > 0.3):
                    better_jobs.append(result[0])
        # print(better_jobs)
        return better_jobs
        return results

              # Empty line for clarity
