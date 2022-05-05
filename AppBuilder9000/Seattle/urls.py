from django.urls import path
from . import views


urlpatterns = [
    path('', views.seattle_home, name='seattle_home'),
    path('create/', views.seattle_create, name='seattle_create'),
    path('view/', views.seattle_view, name='seattle_view')
]