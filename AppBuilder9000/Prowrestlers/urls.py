from django.urls import path
from . import views

urlpatterns = [
    path('', views.wrestlers_home, name='wrestlers_home'),
    path('', views.wrestlers_create, home='wrestlers_create'),
]