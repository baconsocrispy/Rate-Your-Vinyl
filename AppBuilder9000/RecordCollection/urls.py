from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='records_home'),
    path('Records_View/', views.records_view, name='records_view'),
    path('Records_Add/', views.records_add, name='records_add'),
    path('Records_Random/', views.records_random, name='records_random'),
]