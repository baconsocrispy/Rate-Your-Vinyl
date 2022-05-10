from . import views
from django.urls import path


urlpatterns = [
    path('', views.texmex_home, name='texmex_home')
]