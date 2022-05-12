from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity, WeatherMoment
from .forms import ActivityForm, WeatherMomentForm


# Story #1: Build the basic app ---

def oregon_home(request):
    return render(request, 'Oregon_City/Oregon_home.html')

# Story #2: Create your model ----


def oregon_create(request):
    form = ActivityForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../display')
    content = {'form': form}
    return render(request, 'Oregon_City/Oregon_create.html', content)

# Story #3: Display all items from database ----


def oregon_display(request):
    activity = Activity.Entries.all()
    content = {'activity': activity}
    return render(request, 'Oregon_City/Oregon_display.html', content)


def oregon_details(request, pk):
    details = get_object_or_404(Activity, pk=pk)
    content = {'details': details}
    return render(request, 'Oregon_City/Oregon_details.html', content)


def oregon_view(request):
    activity = Activity.Entries.all()
    content = {'Activity': activity}
    return render(request, 'Oregon_City/Oregon_view.html', content)

