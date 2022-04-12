from django.urls import path
from . import views


urlpatterns = [
    path('', views.books_home, name='books_home'),
    path('AddBook/', views.books_addbook, name='books_addbook'),
]