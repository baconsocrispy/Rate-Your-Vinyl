from django.urls import path
from . import views

urlpatterns = [
    path('VideoGamesReviews_Home/', views.VideoGamesReviewsHome, name="VideoGamesReviews_Home"),
]
