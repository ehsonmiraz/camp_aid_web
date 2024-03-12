from django.shortcuts import render
from django.views.generic import ListView
from .models import Job
# Create your views here.
class JobListView(ListView):
    model = Job
    template_name = "jobs/joblist.html"

