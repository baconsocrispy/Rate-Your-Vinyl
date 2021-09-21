from django.urls import path
from . import views

urlpatterns=[
    path('', views.Reading_Home, name='Reading_Home'),
]