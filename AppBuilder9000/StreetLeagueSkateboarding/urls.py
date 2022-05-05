# Imports;
from django.urls import path
from . import views

# URL Patterns;
urlpatterns = [
    # attn: the 'name' has to match the views function here.
    path('', views.SLS_home, name='StreetLeagueSkateboarding_home'),
    path('StreetLeagueSkateboarding_create/', views.SLS_create, name='StreetLeagueSkateboarding_create'),
    path('StreetLeagueSkateboarding_read/', views.SLS_read, name='StreetLeagueSkateboarding_read'),
]