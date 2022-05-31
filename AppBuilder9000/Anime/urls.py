from django.urls import path
from . import views


urlpatterns = [
    path('', views.anime_home, name='anime_home'),
    path('create/', views.create_anime, name='create_anime'),
]



