from django.urls import path
from . import views

urlpatterns = [
    path('', views.stocks_home, name='stocks_home'),
    path('stocks_favorites/', views.favorites, name='stocks_favorites'),
    path('stocks_add_favorites/', views.add_favorites, name='add_favorites'),
]

