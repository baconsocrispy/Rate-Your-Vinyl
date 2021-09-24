from django.urls import path
from . import views

urlpatterns = [
    path('', views.InlineSpeedSkates_Home, name='InlineSpeedSkates_Home'),
]
