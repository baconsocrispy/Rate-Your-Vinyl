from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ArtGallery_home'),
    path('ArtGallery_login/', views.apply, name="ArtGallery_login"),
]
