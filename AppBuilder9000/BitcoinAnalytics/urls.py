from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bitcoin_analytics_home'),
    path('add_competitor/', views.create_competitor, name='create')
]