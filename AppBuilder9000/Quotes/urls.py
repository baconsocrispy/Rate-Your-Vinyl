from django.urls import path, include
from . import views
#API
from rest_framework import routers


urlpatterns = [
    path('', views.home, name='Quotes_home'),
]