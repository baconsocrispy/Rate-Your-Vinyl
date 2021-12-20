from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dnd_characters_home'),
]