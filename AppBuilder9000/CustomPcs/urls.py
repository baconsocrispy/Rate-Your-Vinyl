from django.urls import path
from . import views
from .forms import BuildForm

urlpatterns = [
    path('', views.CustomPcs_home, name='CustomPcs_Home'),
    path('create', views.BuildForm, name='BuildForm.html'),

]
