from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList_Home, name='BookList_Home'),
]