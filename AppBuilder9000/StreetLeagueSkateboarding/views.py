# Imports;
from django.shortcuts import render, redirect
from .models import Skater
from .forms import EntryForm

# Functions;
def SLS_home(request):
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_home.html')

def SLS_create(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("StreetLeagueSkateboarding_home")
    content = {'form': form}
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_create.html', content)

def SLS_read(request):
    entry = Skater.Entry.all()
    content = {'entry': entry}
    return render(request, 'StreetLeagueSkateboarding/StreetLeagueSkateboarding_read.html', content)