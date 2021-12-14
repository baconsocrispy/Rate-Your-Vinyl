from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bitcoin_analytics_home')
]