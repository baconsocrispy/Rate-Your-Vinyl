from django.shortcuts import render

def HikingTrails_home(request):
    return render(request, 'HikingTrails/HikingTrails_home.html')
