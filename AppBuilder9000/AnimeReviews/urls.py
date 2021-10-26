from django.urls import path
from . import views


urlpatterns = [
    path('', views.anime_reviews_home, name='anime_reviews_home'),
]
