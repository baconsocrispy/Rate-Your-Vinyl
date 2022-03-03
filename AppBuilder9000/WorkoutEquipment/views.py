from django.http import HttpResponse
from django.shortcuts import render


def workout_equipment_home(request):
    return render(request, "WorkoutEquipment/WorkoutEquipHome.html")
