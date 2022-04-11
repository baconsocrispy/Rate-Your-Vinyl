from django.urls import path
from . import views

urlpatterns = [
    path('', views.musictaste_home, name='MusicTaste_home'),
]