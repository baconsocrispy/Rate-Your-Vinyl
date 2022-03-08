from django.urls import path

from . import views

urlpatterns = [
    path('', views.Personality_home, name='Personality_home'),
]