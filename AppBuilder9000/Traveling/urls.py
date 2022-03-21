from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.Traveling_home,name='Traveling_home'),
    path('SignUp/', views.Traveling_create, name='Traveling_create')
]