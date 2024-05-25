from django.shortcuts import render, redirect
from job.models import Job
from .user_interface import UserInterface  # Assuming UserInterface is in the same directory
def match_and_display(request):
    ui = UserInterface()
    Jobs,job_skills = ui.get_jobs()
    # print(job_skills)
    # print('Gay')
    results = ui.match_candidates_to_jobs(request)
    # print(results)
    # Jobs = Job.objects.all()
    # ... (process jobs data, prepare for template context)  # Assuming you have further processing
    # print(results)
#     jobs = []
#     for result in results:
#         matching_jobs = Job.objects.filter(title=str(result))  # Filter jobs by title
#   # Check if any jobs were found
#         if matching_jobs:
#             for job in matching_jobs:
#                 print(job.title, end='\n')  # Print each matching job title
#         else:
#             print(f"No job found with title: {result}")  # Handle no matches


    context = {'jobs': results}
    return render(request, 'my_app/result.html',context)