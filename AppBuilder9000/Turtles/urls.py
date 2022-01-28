from django.urls import path
from . import views

urlpatterns = [
    path('', views.turtles_home, name="turtles_home"),
]