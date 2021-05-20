from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ArtGallery_home')
]
