from django.urls import path
from . import views


urlpatterns = [
    path('', views.motorcycling_home, name='motorcycling_home')
]