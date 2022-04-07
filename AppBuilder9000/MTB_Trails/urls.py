from django.urls import path
from . import views


urlpatterns = [
    path('', views.mtb_trails_home, name='mtb_trails_home'),
    path('trails_review/', views.mtb_trails_review, name='mtb_trails_review'),
    path('submitted_review/', views.submitted_review, name='submitted_review'),
    path('existing_reviews/', views.existing_reviews, name='existing_reviews'),
]