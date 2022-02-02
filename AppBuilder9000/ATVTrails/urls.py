from django.urls import path
from . import views

urlpatterns = [
    path('', views.Atv_home, name='Atv_home'),
    path('AtvTrails_create/', views.add_trail, name='add_trail'),
    path('AtvTrails_list/', views.list_trails, name='list_trails'),
    path('AtvTrails_details/', views.trail_details, name='trail_details')
]
