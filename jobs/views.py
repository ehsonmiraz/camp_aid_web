from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Job
from accounts.models import SavedJob,AppliedJob
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class JobListView(ListView):
    model = Job
    template_name = "jobs/joblist.html"
    
    def get_queryset(self):
        category = self.kwargs['category']
        print(category)
        if  category == 'applied':
            return AppliedJob.objects.filter(user_id=self.request.user.id)
        elif category == 'saved':
            saved_jobs= self.request.user.saved_jobs
            
            print(saved_jobs)
        elif category == 'all':
            return Job.objects.all()
        else:
            # Handle other categories or return an empty queryset
            return HttpResponse("No such category")

def save_view(request, id):
    if request.method == 'POST':
      job = Job.objects.get(pk=id)
      saved_job=SavedJob.objects.create(user=request.user,job=job)
      print(saved_job)
      saved_job.save()
    return redirect("jobs:default_list")  

def apply_view(request, id):
    if request.method == 'POST':
      job = Job.objects.get(pk=id)
      applied_job=AppliedJob.objects.create(user=request.user,job=job)
      print(applied_job)
      applied_job.save()
    if job.apply_link:  
        return redirect(job.apply_link)
    else:
        return redirect("https://forms.gle/ERPdSSnLvi57GoEW6")  

