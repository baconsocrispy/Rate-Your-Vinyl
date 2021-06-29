from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .forms import EntryForm
from .models import Entry


def ApexHome(request):#my function that gives the correct html page to load when requested
    return render(request, 'ApexLegendsStats/ApexLegendsStats_home.html')

def EnterStats(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('enterStats')
    else:
        form = EntryForm()
    return render(request, 'ApexLegendsStats/ApexLegendsStats_enterStats.html', {'form': form})

def ViewStats(request):
    statsList = Entry.objects.all()
    return render(request, 'ApexLegendsStats/ApexLegendsStats_viewStats.html', {'statsList': statsList})