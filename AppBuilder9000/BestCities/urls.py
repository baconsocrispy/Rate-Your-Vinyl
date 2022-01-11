from django.urls import path
from . import views

urlpatterns = [
    path('', views.Best_Cities_home, name='Best_Cities_home'),
    ]