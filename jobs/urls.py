from django.contrib import admin
from django.urls import path,include
from .views import *
app_name="jobs"
urlpatterns = [
     path('save/<str:id>/', save_view, name='save_view'),
     path('apply/<str:id>/', apply_view, name='apply_view'),
     path('<str:category>/', JobListView.as_view(), name='list'),
     path('', JobListView.as_view(), {'category': 'all'}, name='default_list'),
]
