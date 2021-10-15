from django.urls import path
from . import views

urlpatterns=[
    path('', views.Oregon_Rocks_Home, name='Oregon_Rocks_Home'),
    path('Rocks_Create/', views.Rocks_Create, name='Rocks_Create'),
    path('Rock_Locations/', views.Rock_Locations, name='Rock_Locations'),
    path('<int:pk>/Rock_Details/', views.Rock_Details, name='Rock_Details'),
]