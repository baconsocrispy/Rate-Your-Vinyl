from django.urls import path
from . import views

urlpatterns = [
    path('', views.Val_home, name='Val_home')
]