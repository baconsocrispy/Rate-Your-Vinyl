from django.urls import path
from . import views

urlpatterns = [
    path('', views.Masonry_home, name='Masonry_home'),
]