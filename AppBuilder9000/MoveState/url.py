from django.urls import path

from . import views

urlpatterns = [
    path('', views.movestate_home, name='movestate_home'),
]