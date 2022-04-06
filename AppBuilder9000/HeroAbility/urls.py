from django.urls import path
from . import views


urlpatterns = [
    path('', views.heroability_home, name='heroability_home'),

]