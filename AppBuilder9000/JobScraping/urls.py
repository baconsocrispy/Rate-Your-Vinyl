from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobScraping_home, name='JobScraping_home'),
    path('input', views.JobScraping_input, name='JobScraping_input'),
    path('inputJob', views.inputJob, name='inputJob'),
    path('savedJobs', views.JobScraping_history, name='JobScraping_history'),
    path('<int:pk>/details/', views.JobScraping_details, name='JobScraping_details'),
    path('<int:pk>/editJob/', views.JobScraping_editJob, name='JobScraping_editJob'),
    path('<int:pk>/saveEdit/', views.saveEdit, name='saveEdit'),
]