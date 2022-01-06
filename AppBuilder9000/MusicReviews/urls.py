from django.urls import path
from . import views


urlpatterns = [
    path('', views.music_reviews_home, name='music_reviews_home'),
    path('Create/', views.createReview, name='createReview'),
    path('review_view/', views.review_view, name='review_view'),

]
