from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.VideoGameReviews_Home, name="VideoGameHome"),
]
