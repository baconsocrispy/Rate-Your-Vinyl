from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnimeHome, name="AnimeHome"),
    path('AnimeReviews/', views.AnimeReviews, name="AnimeReviews"),
    path('AnimeCreate/', views.AnimeCreate, name="AnimeCreate"),
]
