from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.exercises_home, name="Exercises_Home"),
    path('exercises_create/', views.exercises_create, name="exercises_create"),
    path('exercises_names/', views.exercises_names, name="exercises_names"),
    path('exercises_details/<int:pk>/', views.exercises_details, name="exercises_details"),
]