from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.neighborhoodReview_home, name='NeighborhoodReview/NeighborhoodReview_home.html'),
    path('createneighborhood/', views.create_neighborhood, name='NeighborhoodReview/CreateNewNeighborhood.html'),
    path('review/', views.review, name='NeighborhoodReview/CreateReview.html'),
    path('<int:pk>/viewreviews/', views.reviewpage, name='NeighborhoodReview/ReviewPage.html')

]

