
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gardening_home, name='gardening_home'),

]