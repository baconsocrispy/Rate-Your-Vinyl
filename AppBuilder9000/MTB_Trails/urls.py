from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.mtb_trails_home, name='mtb_trails_home'),
]