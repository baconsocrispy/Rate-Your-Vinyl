from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='NoteTaking_home'),
    path('AddNotes/', views.AddNotes, name='NoteTaking_addnotes'),
    path('AddCategories/', views.AddCategories, name='NoteTaking_addcategories'),
    path('<int:pk>/Details/', views.Details, name="NoteTaking_details"),
    path('<int:pk>/Delete/', views.Details, name="NoteTaking_confirmdelete"),
    path('<int:pk>/Edit/', views.Details, name="NoteTaking_confirmedit"),
]
