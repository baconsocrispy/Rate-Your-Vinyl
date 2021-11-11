from django.urls import path

from . import views

urlpatterns = [
    path('', views.hotsprings_home, name='hotsprings_home'),
]