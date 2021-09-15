from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Exercises_Home"),
]

urlpatterns += staticfiles_urlpatterns()