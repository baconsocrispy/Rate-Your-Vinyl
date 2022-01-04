from django.urls import path
from . import views


urlpatterns = [
    path('', views.pet_adoption_home, name='pet_adoption_home'),
    path('list/', views.pet_adoption_list, name='pet_adoption_list'),
]
