from django.urls import path
from . import views

urlpatterns=[
    path('', views.Oregon_Rocks_Home, name='Oregon_Rocks_Home'),
]