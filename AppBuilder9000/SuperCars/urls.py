from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.SuperCarsHome, name='SuperCars_Home'),
    path('<int:pk>/details/', views.details, name="details"),
    path('CreateRecord/', views.CreateRecord, name='CreateRecord'),

]