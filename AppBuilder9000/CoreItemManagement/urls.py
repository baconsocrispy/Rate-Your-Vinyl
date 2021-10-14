# invoking the name while views.'method' page occurs on browser
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cim_home, name="cim_home"),
]