from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobScraping_home, name='JobScraping_home'),
    path('input', views.JobScraping_input, name='JobScraping_input'),
    path('inputJob', views.inputJob, name="inputJob"),
]