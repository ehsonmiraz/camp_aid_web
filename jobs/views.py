from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView,RedirectView
from .models import Job

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.  

class JobListView(LoginRequiredMixin,ListView):
    login_url = 'accounts:login'
    model = Job
    template_name = "jobs/joblist.html"
    
    def get_queryset(self):
        print(type(self.request.user))
        category = self.kwargs['category']
        print(category)
        if  category == 'applied':

            applied_jobs= self.request.user.applied_jobs.all()
            print(applied_jobs)
            return applied_jobs
        elif category == 'saved':
            saved_jobs= self.request.user.saved_jobs.all()
            return saved_jobs
        elif category == 'eligible':
            print(str(self.request.user)+ " "+str(self.request.user.branch))
            eligible_jobs=Job.objects.filter(cgpa__lte=self.request.user.cgpa).filter(eligibility=self.request.user.branch)
            return eligible_jobs
        elif category == 'all' or category == '':
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
    job = Job.objects.get(pk=id)
    if request.method == 'POST':
       request.user.applied_jobs.add(job)         
       request.user.save() 
       if job.apply_link:  
         return redirect(job.apply_link)
    
    return  HttpResponse("This post is not available")

