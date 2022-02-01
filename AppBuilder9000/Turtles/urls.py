from django.urls import path
from . import views

# Stores url patterns to determine which Views functions to call
urlpatterns = [
    path('', views.turtles_home, name='turtles_home'),  # Default if there is no path.
    path('create/', views.turtles_create, name='turtles_create'),  # Path to 'turtles_create.html'
]
