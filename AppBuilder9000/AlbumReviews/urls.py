from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="AlbumReviews_home.html"),
]