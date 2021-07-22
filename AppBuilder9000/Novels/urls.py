from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="Novels_home"),
    path('Novels_create/', views.novelEntry, name="Novels_create"),
    path('Novels_display/', views.novelDisplay, name="Novels_display")
]