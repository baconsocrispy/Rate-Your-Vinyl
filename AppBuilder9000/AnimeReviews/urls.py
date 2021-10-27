from django.urls import path
from . import views


urlpatterns = [
    path('', views.anime_reviews_home, name='anime_reviews_home'),
    path('anime_reviews_create/', views.anime_reviews_create, name="anime_reviews_create"),
]
