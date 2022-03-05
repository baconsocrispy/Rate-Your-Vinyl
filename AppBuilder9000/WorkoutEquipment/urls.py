from django.urls import path
from . import views

#  url patterns to determine which view function to call
urlpatterns = [
    path('', views.workout_equipment_home, name='WorkoutEquipHome'),  #default, no path
    path('WorkoutEquipConsole/', views.workout_equip_console, name='workout_equip_console'), # path to console
    path('WorkoutEquipCreate/', views.workout_equip_create, name='workout_equip_create'),
    path('WorkoutEquipDisplay', views.workout_equip_display, name='workout_equip_display'),
    # path('<int:pk>/workout_equip_details/', views.workout_equip_details, name='workout_equip_details'),
    ]