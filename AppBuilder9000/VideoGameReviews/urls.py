from django.urls import path
from . import views

urlpatterns = [
    path('', views.videogamereviews, name="VideoGamesReview_Home"),
]
