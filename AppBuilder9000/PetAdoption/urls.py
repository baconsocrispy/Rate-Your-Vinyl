from django.urls import path
from . import views


urlpatterns = [
    path('', views.pet_adoption_home, name='pet_adoption_home'),
]
