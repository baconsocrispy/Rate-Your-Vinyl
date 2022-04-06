from django.urls import path
from . import views


urlpatterns = [
    path('', views.heroability_home, name='heroability_home'),
    path('new_hero/', views.heroability_new_hero, name='heroability_new_hero'),

]