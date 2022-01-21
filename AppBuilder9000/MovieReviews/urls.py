from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name="moviereviews_home"),
    path('moviereviews_create/', views.moviereviews_create, name="moviereviews_create"),
    path('moviereviews_display/', views.moviereviews_display, name="moviereviews_display"),
]


