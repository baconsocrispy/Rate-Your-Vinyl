from django.urls import path
from .import views


urlpatterns = [
    path('', views.GrandmasRecipes_home, name='GrandmasRecipes_home'),
    #path('/library', views.GrandmasRecipes_library, name='GrandmasRecipes_library')
    #path('/AddNew', views.GrandmasRecipes_library, name='GrandmasRecipes_library')
]
