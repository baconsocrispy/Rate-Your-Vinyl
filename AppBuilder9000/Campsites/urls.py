from django.urls import path
from .import views

urlpatterns = [
    path('', views.campsites_home, name='campsites_home'),
    path('campsites_create/', views.add_campsites, name='campsites_create'),
    path('campsites_list/', views.list_campsites, name='campsites_list'),
    path('<int:pk>/campsites_details/', views.campsites_details, name='campsites_details'),
]