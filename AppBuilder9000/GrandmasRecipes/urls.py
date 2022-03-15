from django.urls import path
from . import views

# the directory of . is our current directory
# so the above says import views.py from the current directory
# ANATOMY OF A URL ROUTE:
# ('pattern to watch for',method to call,"shortcut name")

urlpatterns = [
    path('', views.grandmas_home, name='GrandmasRecipes_home'),
    path('create', views.grandmas_create, name='GrandmasRecipes_create'),
    path('cookbook', views.grandmas_cookbook, name='GrandmasRecipes_cookbook'),
]
