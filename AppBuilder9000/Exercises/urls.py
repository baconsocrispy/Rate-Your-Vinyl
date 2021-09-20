from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercises_home, name="Exercises_Home"),
    path('exercises_names', views.exercises_names, name="exercises_names"),
    path('<int:pk>/exercises_details/', views.exercises_details, name="exercises_details"),
    path('<int:pk>/exercises_delete/', views.exercises_delete, name="exercises_delete"),
    path('exercises_deleteConfirm/', views.exercises_deleteConfirm, name="exercises_deleteConfirm"),
    path('exercises_create/', views.exercises_create, name="exercises_create"),
]
