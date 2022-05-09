from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobsHome, name='jobsHome'),
    path('create/', views.jobsCreate, name='jobsCreate'),

]