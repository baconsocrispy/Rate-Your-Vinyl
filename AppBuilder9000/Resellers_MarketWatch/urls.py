from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('AccountPage/', views.account, name='Account'),
    path('About/', views.about , name='About'),
    path('News/', views.news , name='News'),
    path('Register/', views.register, name='Register'),
    # path('/', views. , name=''),
]


# path('create/', views.create_account, name='create'),