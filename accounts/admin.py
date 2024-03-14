from django.contrib import admin
from .models import StudentUser,SavedJob,AppliedJob
# Register your models here.
admin.site.register(StudentUser)
admin.site.register(SavedJob)
admin.site.register(AppliedJob)