from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='SportsCards_home'),
    path('join/', views.join, name='SportsCards_join'),
    path('display/', views.display, name="SportsCards_display"),
    path('details/', views.details, name="SportsCards_details"),
    path('delete/', views.delete, name="SportsCards_delete"),
]
