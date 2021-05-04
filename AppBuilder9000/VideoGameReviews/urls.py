from django.urls import path
from . import views

urlpatterns = [
    path('', views.videogamereviews, name="VideoGamesReview_Home"),
    path('VideoGamesReviews_Reviews/', views.videoreviews, name="VideoGamesReviews_Reviews.html"),
]
