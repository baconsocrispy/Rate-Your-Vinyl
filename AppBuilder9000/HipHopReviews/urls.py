from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='HipHopReviews_home'),
    path('request', views.request, name='HipHopReviews_request'),
    path('reviews', views.reviews, name='HipHopReviews_reviews'),
]