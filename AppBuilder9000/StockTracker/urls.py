from . import views
from django.urls import path

urlpatterns = [
    path('', views.stock_home_page, name='stock_home'),

]