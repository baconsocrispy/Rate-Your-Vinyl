from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AlbumReviews_home, name="AlbumReviews_home"),
    path('add/', views.AlbumReviews_add, name="AlbumReviews_add"),
    path('list/', views.AlbumReviews_list, name="AlbumReviews_list"),
]