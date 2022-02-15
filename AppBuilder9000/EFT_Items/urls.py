from django.urls import path
from . import views

urlpatterns = [
    path('', views.eft_home, name="eft_items_home"),
]
