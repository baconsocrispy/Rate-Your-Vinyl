from django.urls import path
from . import views

urlpatterns = [
    path('', views.StarWatch_home, name='StarWatch_home'),
    path('StarWatch_addObject/', views.add_object, name='StarWatch_addObject'),
]