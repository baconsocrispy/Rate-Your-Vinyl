from django.urls import path
from . import views

urlpatterns = [
    path('', views.dfort_home, name='dfort_home'),
    path('create/', views.dfort_create, name='dfort_create'),
    path('display/', views.dfort_display, name='dfort_display'),
    path('<int:pk>/details/', views.dfort_details, name='dfort_details'),
    path('search/', views.dfort_search, name='dfort_search'),
]