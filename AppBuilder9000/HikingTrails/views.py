from django.shortcuts import render, redirect
from .forms import TrailsForm
from .models import Trails


def HikingTrails_home(request):
    return render(request, 'HikingTrails/HikingTrails_home.html')


def HikingTrails_create(request):
    form = TrailsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('HikingTrails_home')
    content = {'form': form}
    return render(request, 'HikingTrails/HikingTrails_create.html', content)


def HikingTrails_display(request):
    hiking_trails = Trails.Trail.all()
    content = {'trails': hiking_trails}
    return render(request, 'HikingTrails/HikingTrails_display.html', content)
