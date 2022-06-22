from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('', views.MusicReviews_home, name='MusicReviews_home'),
    path('AddMusic/', views.MusicReviews_AddMusic, name='MusicReviews_Add_Music'),
    path('<int:pk>/Details/', views.MusicReviews_details, name='music_details'),
    path('MusicReviews/', views.MusicReviews_reviews, name='MusicReviews_reviews'),
    path('<int:pk>/Delete/', views.MusicReviews_delete, name='Music_delete'),
    path('<int:pk>/Update/', views.MusicReviews_update, name='MusicReviews_update'),
]
