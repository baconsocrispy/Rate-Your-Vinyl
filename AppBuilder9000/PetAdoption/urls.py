from django.urls import path
from . import views


urlpatterns = [
    path('', views.pet_adoption_home, name='pet_adoption_home'),
    path('/list/', views.pet_adoption_list, name='pet_adoption_list'),
    path('/dogs/', views.pet_adoption_dogs, name='pet_adoption_dogs'),
    path('/cats/', views.pet_adoption_cats, name='pet_adoption_cats'),
    path('/other/', views.pet_adoption_other, name='pet_adoption_other'),
    path('/all/', views.pet_adoption_all, name='pet_adoption_all'),
]
