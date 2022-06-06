from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobScraping_home, name='JobScraping_home'),
]