from django.urls import path
from . import views


urlpatterns = [
    path('', views.music_reviews_home, name='musicreviews_home'),
]
