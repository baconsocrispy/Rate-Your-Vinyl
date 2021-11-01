from django.urls import path
from . import views


urlpatterns = [
    path('', views.anime_reviews_home, name='anime_reviews_home'),
    path('anime_reviews_create/', views.anime_reviews_create, name="anime_reviews_create"),
    path('anime_reviews_view/', views.anime_reviews_view, name="anime_reviews_view"),
    path('<int:pk>/anime_reviews_details/', views.anime_reviews_details, name="anime_reviews_details"),
    path('<int:pk>/anime_reviews_edit/', views.anime_reviews_edit, name="anime_reviews_edit"),
]
