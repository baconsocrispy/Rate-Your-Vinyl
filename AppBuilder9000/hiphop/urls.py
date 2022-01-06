from django.urls import path
from AppBuilder9000.Hiphop.templates.hiphop import views


urlpatterns = [
    path('', views.hiphop_home, name='hiphop_home'),
]
