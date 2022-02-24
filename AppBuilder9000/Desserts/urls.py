from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='desserts_home'),
    path('desserts_add/', views.add_recipe, name='desserts_add'),
]