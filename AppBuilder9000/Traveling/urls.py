from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.Traveling_home,name='Traveling_home'),
    path('SignUp/', views.Traveling_create, name='Traveling_create'),
    path('Flights/', views.Traveling_place, name='Traveling_place'),
    path('<int:pk>/viewdetails/' ,views.detail_view, name='details_view'),
    path('<int:pk>/details/', views.details, name='details'),
]
