from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="AlbumReviews_home"),
    path('add/', views.add, name="AlbumReviews_add"),
]