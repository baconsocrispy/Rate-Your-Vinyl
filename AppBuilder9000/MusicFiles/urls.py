from django.urls import path
from . import views


urlpatterns = [
    path('', views.musicfiles_home, name='musicfiles_home'),
    path('create', views.musicfiles_create, name="Create"),
]