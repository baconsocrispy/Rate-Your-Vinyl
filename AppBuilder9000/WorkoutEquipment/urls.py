from django.urls import path
from . import views

#  url patterns to determine which view function to call
urlpatterns = [
    path('', views.workout_equipment_home, name='WorkoutEquipHome'),
    ]