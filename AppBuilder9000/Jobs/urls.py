from django.urls import path
from . import views

urlpatterns = [
    path('', views.coachHome, name='coachHome'),
    path('create/', views.coachCreate, name='coachCreate'),
    path('signups/', views.childCreate, name='coachChildSignups'),


]