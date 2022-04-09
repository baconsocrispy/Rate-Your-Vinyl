from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib import messages
from .forms import ResultForm
from .models import Result

##ADDING IN ALL DATA NEEDED FOR POINT CALCULATIONS

POINTS_PER_POSITION_FEATURE = {
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

POINTS_PER_POSITION_SPRINT = {
    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 3,
    7: 2,
    8: 1,
}

# RENDERS HOME PAGE
def f1_home(request):
    return render(request, "Formula1/Formula1_home.html")

# RENDERS DISPLAY RACE RESULTS PAGE
def race_results(request):
    data = Result.results.all().order_by('Race', 'Race_Type', '-Points_Earned')
    return render(request, "Formula1/Formula1_raceResults.html", {'data': data})

def driver_results(request):
    data = Result.results.all()
    total_points = 0
    driver_tracker = {}
    for result in data:
        if result.Driver_Name not in driver_tracker:
            driver_tracker[result.Driver_Name] = {'team': result.Current_Team, 'total': int(result.Points_Earned)}
        else:
            points = driver_tracker[result.Driver_Name]['total']
            driver_tracker[result.Driver_Name]['total'] = int(result.Points_Earned) + points
    drivers_sorted_list = sorted(driver_tracker.items(), key= lambda x: x[1]['total'], reverse=True)
    drivers_sorted = {}
    for item in drivers_sorted_list:
        drivers_sorted[item[0]] = {list(item[1].keys())[0]:item[1]['team'], list(item[1].keys())[1]:item[1]['total']}

    context = {
        'drivers_sorted': drivers_sorted,
        'total_points': total_points,
        'data': data
    }
    return render(request, "Formula1/Formula1_driverResults.html", context)

# RENDERS DISPLAY TEAM RESULTS PAGE
def team_results(request):
    data = Result.results.all()
    total_points = 0
    team_tracker = {}
    for result in data:
        if result.Current_Team not in team_tracker:
            team_tracker[result.Current_Team] = {'total': int(result.Points_Earned)}
        else:
            points = team_tracker[result.Current_Team]['total']
            team_tracker[result.Current_Team]['total'] = int(result.Points_Earned) + points
    teams_sorted_list = sorted(team_tracker.items(), key= lambda x: x[1]['total'], reverse=True)
    teams_sorted = {}
    for item in teams_sorted_list:
        teams_sorted[item[0]] = {list(item[1].keys())[0]:item[1]['total']}

    context = {
        'teams_sorted': teams_sorted,
        'total_points': total_points,
        'data': data
    }
    return render(request, "Formula1/Formula1_teamResults.html", context)

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
            key = f"{result.Race} - {result.Race_Type} - {result.Driver_Name}"
            result.Driver_Race_Key = key
            # USE BUSINESS LOGIC TO CALCULATE POINT TOTAL
            if result.Finishing_Position == 'DNF':
                result.Points_Earned = 0
            else:
                pos = int(result.Finishing_Position)
                if result.Race_Type == 'Feature Race':
                    if pos <= 10:
                        points = POINTS_PER_POSITION_FEATURE[pos]
                        if result.Fastest_Lap == True:
                            points = points + 1
                        result.Points_Earned = points
                    else:
                        result.Points_Earned = 0
                else:
                    if pos <=8:
                        points = POINTS_PER_POSITION_SPRINT[pos]
                        result.Points_Earned = points
                    else:
                        result.Points_Earned = 0
            ##SAVE ALL DATA TO RESULTS MODEL AND RETURN AN ERROR IF A RESULT HAS ALREADY BEEN RECORDED FOR THAT RACE+DRIVER COMBO
            try:
                result.save()
                messages.success(request, "Result was successfully saved.")
                return redirect('add_result')
            except IntegrityError as e:
                messages.error(request, f"{result.Driver_Name} already has a result recorded for {result.Race} - {result.Race_Type}")
                return redirect('add_result')
        else:
            print(form.errors)
    else:
        messages.error("Error. Result not saved.")
        return redirect('add_result')
