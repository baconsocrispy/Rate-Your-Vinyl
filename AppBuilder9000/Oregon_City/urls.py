from django.urls import path
from . import views

urlpatterns = [
    path('', views.oregon_home, name='Oregon_home'),
]