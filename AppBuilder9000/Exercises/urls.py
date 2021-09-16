from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="Exercises_Home"),
    path('exercises_create/', views.create, name="exercises_create"),
]