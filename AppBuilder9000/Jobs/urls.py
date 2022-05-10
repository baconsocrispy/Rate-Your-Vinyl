from django.urls import path
from . import views

urlpatterns = [
    path('', views.coachHome, name='coachHome'),
    path('create/', views.coachCreate, name='coachCreate'),
    path('signups/', views.childCreate, name='coachChildSignups'),
    path('fullroster/', views.childRoster, name='coachChildRoster'),
    path('childdetails/', views.childDetails, name='coachChildDetails'),


]