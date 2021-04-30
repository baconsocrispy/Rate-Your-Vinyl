from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.VideoGamesReviews_Home, name="VideoGameHome"),
]
