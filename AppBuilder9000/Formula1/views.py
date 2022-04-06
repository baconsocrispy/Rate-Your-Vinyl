from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib import messages
from .forms import ResultForm
from .models import Team, Race, Driver, Result

POINTS_PER_POSITION = {
    1: 25,
    2: 18,
    3: 15,
    4: 12,
    5: 10,
    6: 8,
    7: 6,
    8: 4,
    9: 2,
    10: 1,
}

# RENDERS HOME PAGE
def f1_home(request):
    return render(request, "Formula1/Formula1_home.html")

# RENDERS ADD RESULT PAGE
def add_result(request):
    form = ResultForm()
    return render(request, "Formula1/Formula1_addResult.html", {'form': form})

# HANDLES FORM DATA FROM ADD RESULT PAGE
def result_submit(request):
    form = ResultForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            result = form.save(commit=False)
            # GENERATE DRIVER_RACE_KEY AND ASSIGN IT
            key = f"{result.Race} - {result.Driver_Name}"
            result.Driver_Race_Key = key
            # USE DRIVER DATA FROM USER TO ASSIGN THE CORRECT TEAM, USING DATA FROM DRIVER MODEL
            team = Driver.drivers.filter(Driver_Name=result.Driver_Name).values('Current_Team').first()
            result.Current_Team = team['Current_Team']
            # USE BUSINESS LOGIC TO CALCULATE POINT TOTAL
            if result.Finishing_Position == 'DNF':
                result.Points_Earned = 0
            else:
                pos = int(result.Finishing_Position)
                if pos <= 10:
                    points = POINTS_PER_POSITION[pos]
                    if result.Fastest_Lap == True:
                        points = points + 1
                    result.Points_Earned = points
                else:
                    result.Points_Earned = 0
            try:
                result.save()
                messages.success(request, "Result was successfully saved.")
                return redirect('add_result')
            except IntegrityError as e:
                messages.error(request, f"{result.Driver_Name} already has a result recorded for {result.Race}")
                return redirect('add_result')
        else:
            print(form.errors)
    else:
        messages.error("Error. Result not saved.")
        return redirect('add_result')