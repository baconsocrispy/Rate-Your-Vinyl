from django.urls import path
from . import views

# Stores url patterns to determine which Views functions to call
urlpatterns = [
    path('', views.turtles_home, name="turtles_home"),
    path('create/', views.turtles_create, name="turtles_create"),
]