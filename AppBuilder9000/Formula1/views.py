from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
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

# Create your views here.
def f1_home(request):
    return render(request, "Formula1/Formula1_home.html")

def add_result(request):
    form = ResultForm()
    return render(request, "Formula1/Formula1_addResult.html", {'form': form})

def result_submit(request):
    form = ResultForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            result = form.save(commit=False)
            team = Driver.drivers.filter(Driver_Name=result.Driver_Name).values('Current_Team')
            result.Current_Team = team['Current_Team']
            if result.Finishing_Position >= 10:
                points = POINTS_PER_POSITION[result.Finishing_Position]
                if result.Fastest_Lap == True:
                    points = points + 1
                result.Points_Earned = points
            else:
                result.Points_Earned = 0
            result.save()
            print("Result was successfully saved")
            return redirect('f1_home')
        else:
            print(form.errors)
    else:
        print("Wrong request method")
        return redirect('f1_home')