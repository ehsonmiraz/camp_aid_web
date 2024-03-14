from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Job

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class JobListView(ListView):
    model = Job
    template_name = "jobs/joblist.html"
    
    def get_queryset(self):
        print(type(self.request.user))
        category = self.kwargs['category']
        print(category)
        if  category == 'applied':      
            applied_jobs= self.request.user.applied_jobs.all()
            return applied_jobs
        elif category == 'saved':
            saved_jobs= self.request.user.saved_jobs.all()
            return saved_jobs
        elif category == 'eligible':
            eligible_jobs=Job.objects.filter(cgpa__lte=self.request.user.cgpa).filter(eligibility=self.request.user.branch)
            return eligible_jobs
        elif category == 'all':
            return Job.objects.all()
        else:
            # Handle other categories or return an empty queryset
            return HttpResponse("No such category")

def save_view(request, id):
    if request.method == 'POST':
      job = Job.objects.get(pk=id)
      print("job: "+ str(job))
      try:
        if(request.user.saved_jobs.get(id=job.id)):
          request.user.saved_jobs.remove(job)       
      except Exception:
          request.user.saved_jobs.add(job) 
          
      request.user.save()
      
    return redirect("jobs:default_list")  

def apply_view(request, id):
    if request.method == 'POST':
      job = Job.objects.get(pk=id)
      applied_jobs=request.user.applied_jobs.add(job)
      print(applied_jobs)
      applied_jobs.save()
    if job.apply_link:  
        return redirect(job.apply_link)
    else:
        return redirect("https://forms.gle/ERPdSSnLvi57GoEW6")  

