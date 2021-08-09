from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='SportsCards_home'),
]