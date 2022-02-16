from django.urls import path
from . import views

urlpatterns = [
    path('', views.eft_home, name="eft_items_home"),
    path('create/', views.eft_create_record, name="eft_create_record"),
]
