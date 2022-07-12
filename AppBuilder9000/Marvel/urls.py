from django.urls import path
from . import views

urlpatterns = [
    path('', views.marvel_home, name='marvel_home'),
]
