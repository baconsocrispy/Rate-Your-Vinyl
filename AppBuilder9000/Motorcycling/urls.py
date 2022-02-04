from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('', views.motorcycling_home, name="motorcycling_home"),
    path('rate_motorcycle/', views.create_motorcycle, name="rate_motorcycle"),
    path('rate_route/', views.create_route, name="rate_route"),
    path('create_motorcycle_record/', views.create_motorcycle, name="create_motorcycle_record"),
    path('admin_console', views.admin_console, name="admin_console"),
]

