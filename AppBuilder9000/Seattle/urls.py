from django.urls import path
from . import views


urlpatterns = [
    path('', views.seattle_home, name='seattle_home')
]