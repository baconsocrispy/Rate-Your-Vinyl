from django.urls import path
from . import views


urlpatterns = [
    path('', views.resorts_home, name='resorts_home')

]