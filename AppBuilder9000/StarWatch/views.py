from django.shortcuts import render, redirect
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from .forms import form_addObject
from .models import celestialObject

# Create your views here.
from django.http import HttpResponse


def StarWatch_home(request):
    return render(request, 'StarWatch/StarWatch_home.html')


def add_object(request):
    form = form_addObject(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('StarWatch_addObject')
    content = {'form': form}
    return render(request, 'StarWatch/StarWatch_addObject.html', content)


def MMACreate(request):
    form = ChampForm(data=request.POST or None)
    # if form data is valid
    if request.method=='POST':
        if form.is_valid():
            # save form data to our model
            form.save()
            return redirect('MMA_Create')

    context = {'form': form}
    return render(request, "MMAStats/MMA_create.html", context)





