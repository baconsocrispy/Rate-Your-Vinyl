from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList_Home, name='BookList_Home'),
    path('Book_Entry/', views.Book_Entry, name='BookList_Create'),
]
