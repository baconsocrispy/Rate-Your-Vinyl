from django.urls import path
from . import views

urlpatterns = [
    path('', views.Atv_home, name='Atv_home'),
]
