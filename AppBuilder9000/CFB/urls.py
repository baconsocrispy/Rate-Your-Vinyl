from django.urls import path
from . import views


urlpatterns = [
    path('', views.CFB_Home, name='CFB_Home'),
]