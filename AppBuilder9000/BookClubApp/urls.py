from django.urls import path
from . import views

# create url paths
urlpatterns = [
    path('', views.BookClubApp_home, name='BookClubApp_home'),
    path('booklist/', views.BookClubApp_booklist, name='BookClubApp_bookList'),
    path('wishlist/', views.BookClubApp_explore, name='BookClubApp_explore'),
    path('addbook/', views.BookClubApp_AddBook, name='BookClubApp_AddBook'),
    path('book/<int:pk>', views.BookClubApp_book, name='BookClubApp_book'),
    path('book/<int:pk>/edit/', views.BookClubApp_edit, name='BookClubApp_edit'),
    path('book/<int:pk>/delete/', views.BookClubApp_delete, name='BookClubApp_delete'),
    path('search/', views.BookClubApp_searchForm, name='BookClubApp_searchForm'),
]