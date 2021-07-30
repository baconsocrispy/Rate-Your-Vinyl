from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.neighborhoodReview_home, name='NeighborhoodReview/NeighborhoodReview_home.html'),
    path('createneighborhood/', views.create_neighborhood, name='NeighborhoodReview/CreateNewNeighborhood.html'),
    path('review/', views.review, name='NeighborhoodReview/CreateReview.html'),
    path('<int:pk>/viewreviews/', views.reviewpage, name='NeighborhoodReview/ReviewPage.html'),
    path('neighborhood_details/', views.details, name='NeighborhoodReview/DisplayAllNeighborhoods.html'),
    path('<int:pk>/neighborhood_item_details/', views.item_details, name='DisplayNeighborhood_item.html'),
    path('<int:pk>/edit_neighborhood/', views.edit_neighborhood, name='NeighborhoodReview/edit.html'),
    path('<int:pk>/DeleteNeighborhood/', views.delete_neighborhood, name='NeighborhoodReview/DeleteNeighborhood.html')
]

