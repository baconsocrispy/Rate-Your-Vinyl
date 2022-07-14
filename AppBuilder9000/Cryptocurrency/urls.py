from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cryptocurrency_home, name='Cryptocurrency_home'),
    path('AddReview/', views.cryptocurrency_addreview, name='Cryptocurrency_AddReview'),
    path('Reviews/', views.cryptocurrency_reviews, name='Cryptocurrency_Reviews'),
    path('<int:pk>/Details/', views.cryptocurrency_details, name='Cryptocurrency_Details'),
]
