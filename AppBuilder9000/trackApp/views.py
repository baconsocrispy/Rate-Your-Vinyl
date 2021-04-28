from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from .forms import TrackForm
from .models import Track

def TrackApp_home(request):
    return render,(request,"TrackApp_home.html")

def Create_Tracking(request):
    form = TrackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('')
    else:
        print(form.errors)
        form = TrackForm()
    context = {
        'form': form,
    }
    return render(request, 'TrackApp/TrackApp_newitem.html', context)








