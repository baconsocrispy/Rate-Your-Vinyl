from django.urls import path
from . import views

urlpatterns = [
    path('', views.speed_run_home, name='speed_run_home'),
]
