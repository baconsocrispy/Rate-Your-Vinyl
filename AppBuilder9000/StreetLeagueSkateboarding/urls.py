# Imports;
from django.urls import path
from . import views

# URL Patterns;
urlpatterns = [
    path('', views.SLS_home, name='StreetLeagueSkateboarding_home'),
    path('StreetLeagueSkateboarding_create/', views.SLS_create, name='StreetLeagueSkateboarding_create'),
    path('StreetLeagueSkateboarding_view/', views.SLS_view, name='StreetLeagueSkateboarding_view'),
    path('<int:pk>/StreetLeagueSkateboarding_details/', views.SLS_details, name='StreetLeagueSkateboarding_details'),
]