from django.urls import path
from . import views

urlpatterns = [
    path('', views.IceHockey_home, name='IceHockey_home'),
]