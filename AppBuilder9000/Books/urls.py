from django.urls import path
from . import views

# urls which point to function in views.py
urlpatterns = [
    path('', views.books_home, name='books_home'),
    path('AddBook/', views.books_add_book, name='books_add_book'),
    path('Reviews/', views.books_reviews, name='books_reviews'),
]