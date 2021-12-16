from django.urls import path
from . import views

urlpatterns = [
    path('', views.stocks_home, name='stocks_home'),
]