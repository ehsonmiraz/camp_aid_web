from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from jobs.models import  Job
class StudentUser(AbstractUser):
    
    branch_choices={
                    'BTCSE24':'Btech Computer Science 24',
                    'BTME24':'Btech Mechanical 24',
                    'BTCE24':'Btech Civil 24',
                    'BTPE24':'Btech Petroleum 24',
                    'BTEE24':'Btech Electrical 24',
                    'BTECE24':'Btech Electronic and communication 24'
    }
    cgpa = models.FloatField(blank=True, null=True)
    branch  = models.CharField(
        max_length=10,
        choices=branch_choices,
        default="BTCSE24",
    )
    roll_no = models.CharField(max_length=20, blank=True)
    applied_jobs = models.ManyToManyField(Job, through='AppliedJob', related_name='applying_users', blank=True)
    saved_jobs = models.ManyToManyField(Job, through='SavedJob', related_name='saving_users', blank=True)

    def __str__(self):
        return self.username
   
class AppliedJob(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.user} applied {self.job}'

class SavedJob(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} saved {self.job}'

    