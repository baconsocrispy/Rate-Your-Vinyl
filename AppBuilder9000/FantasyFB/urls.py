from django.urls import path

from . import views

urlpatterns = [
    path('', views.fantasyFB_home, name='fantasyFB_home'),
    path('fantasyFB_form/', views.fantasyFB_form, name='fantasyFB_form'),
]
