from django.urls import path
from . import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.MusicReviews_home, name='MusicReviews_home'),
    # path('AddMusic/', views.MusicReviews_addmusic, name='musicReviews_add_music'),
    # path('MusicReviews/', views.MusicReviews_reviews, name='MusicReviews_reviews'),
    # path('<int:pk>/Delete/', views.MusicReviews_delete, name='Music_delete'),
    # path('<int:pk>/Update/', views.MusicReviews_update, name='MusicReviews_update'),
]
