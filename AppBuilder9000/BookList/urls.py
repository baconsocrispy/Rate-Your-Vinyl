from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList_Home, name='BookList_Home'),
    path('Book_Entry/', views.Book_Entry, name='BookList_Create'),
    path('Book_Display/', views.BookList_Display, name='BookList_Display'),
]
