from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bitcoin_analytics_home'),
    path('/add_competitor/', views.create_competitor, name='create'),
    path('/board/', views.show_competition, name='board'),
    # path('competitor_details/', views.show_details, name='details')
]