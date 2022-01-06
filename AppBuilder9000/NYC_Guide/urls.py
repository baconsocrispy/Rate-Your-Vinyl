from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='nyc_guide_home'),
]