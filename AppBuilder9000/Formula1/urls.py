from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.f1_home, name="f1_home"),
    path('add_result/', views.add_result, name="add_result"),
    path('race_results/', views.race_results, name="race_results"),
    path('driver_results/', views.driver_results, name="driver_results"),
    path('team_results/', views.team_results, name="team_results"),
    path('result_submit/', views.result_submit, name="result_submit"),
    path('admin/', admin.site.urls),
]