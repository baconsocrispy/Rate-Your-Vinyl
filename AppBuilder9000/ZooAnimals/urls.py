from django.urls import path
from . import views

urlpatterns = [
    path('home', views.zoo_home, name='zoo_home'),
    path('add', views.zoo_add, name='zoo_add'),
    path('current', views.zoo_current, name='zoo_current'),
    path('<id>', views.zoo_details, name='zoo_details'),
]