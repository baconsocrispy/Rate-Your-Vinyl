from django.urls import path
from . import views

urlpatterns = [
    path('', views.dfort_home, name='dfort_home')
]