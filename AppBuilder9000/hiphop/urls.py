from django.urls import path
from . import views


urlpatterns = [
    path('', views.hiphop_home, name='hiphop_home'),
]
