from django.urls import path
from . import views

urlpatterns = [
    path('', views.masonry_home, name='masonry_home'),
]