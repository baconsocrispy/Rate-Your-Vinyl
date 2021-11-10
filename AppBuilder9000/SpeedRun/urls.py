from django.urls import path
from . import views

urlpatterns = [
    path('', views.speed_run_home, name='speed_run_home'),
    path('speed_run_create/', views.add_record, name='speed_run_create'),
    path('speed_run_create_game/', views.add_game, name='speed_run_create_game'),
]
