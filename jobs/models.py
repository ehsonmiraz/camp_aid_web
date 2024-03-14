from django.db import models
from django.urls import reverse

# Create your models here.
class Job(models.Model):
    objects = models.Manager()
    organization=models.CharField(max_length=30)
    date=models.DateField(auto_now_add=True)
    location=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    cgpa=models.FloatField(default=0.0, blank=True)
    salary=models.IntegerField(blank=True, null=True)
    position=models.CharField(max_length=30)
    apply_link=models.URLField(blank=True, null=True)

    def __str__(self):
        return self.organization + self.position

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class ArchivedJob(models.Model):
    objects = models.Manager()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    archived_at = models.DateTimeField(auto_now_add=True)