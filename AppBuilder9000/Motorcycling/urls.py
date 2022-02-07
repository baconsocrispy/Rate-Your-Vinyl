from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('', views.motorcycling_home, name="motorcycling_home"),
    path('rate_motorcycle/', views.create_motorcycle, name="rate_motorcycle"),
    path('rate_route/', views.create_route, name="rate_route"),
    path('list_motorcycles/', views.all_motorcycles, name="list_motorcycles"),
    path('admin_console/', views.admin_console, name="admin_console"),
    path('list_routes/', views.all_routes, name="list_routes"),
]

