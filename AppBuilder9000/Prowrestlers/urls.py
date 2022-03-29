from django.urls import path
from . import views

urlpatterns = [
    path('', views.wrestlers_home, name='wrestlers_home'),
    path('ProWrestling_createpage/', views.add_prowrestler, name='wrestlers_create'),
]