from django.urls import path
from . import views

urlpatterns = [
    path('', views.TrackApp_home, name="TrackApp_home")
]