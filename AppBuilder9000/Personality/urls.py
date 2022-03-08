from django.urls import path

from . import views

urlpatterns = [
    path('', views.personality_home, name='personality_home'),
]