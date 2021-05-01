from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('AccountPage/', views.account, name='Account'),
    path('Register/', views.register, name='Register'),
]