from django.urls import path
from . import views

urlpatterns = [
    path('', views.eft_home, name="eft_items_home"),
    path('create/', views.eft_create_record, name="eft_create_record"),
    path('display_items/', views.eft_all_items, name="eft_all_items"),
    path('<int:pk>/details/', views.eft_details, name="eft_item_details"),
]
