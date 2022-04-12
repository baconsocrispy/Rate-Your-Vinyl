from django.urls import path
from . import views


urlpatterns = [
    path('', views.heroability_home, name='heroability_home'),
    path('new_hero/', views.heroability_new_hero, name='heroability_new_hero'),
    path('records/', views.heroability_display_all, name='heroability_display_all'),
    path('<int:pk>/details/', views.heroability_details, name='heroability_details'),
    path('confirm_delete/', views.heroability_confirm_delete, name='heroability_confirm_delete'),

]
