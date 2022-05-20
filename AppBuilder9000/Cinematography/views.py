from django.http import HttpResponse
from .forms import cameraForm
from .models import FieldOfView
from django.shortcuts import render, redirect, get_object_or_404


def camIndex(request):
    form = cameraForm(data=request.POST or None)
    if request.method == 'POST':
        return addCamera(request)
    content = {'form': form}
    return render(request, "Camera_home.html", content)


def addCamera(request):
    form = cameraForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Camera_home')
    content = {'form': form}
    return render(request, "Camera_home.html", content)


def camList(request, pk):
    pullCam = get_object_or_404(FieldOfView, pk=pk)
    content = {'pullCam': pullCam}
    return render(request, "Camera_database.html", content)


def navbar(request):
    return render(request, "content/navbar.html")


def colors(request):
    return render(request, "content/colors.html")


def comp(request):
    return render(request, "content/comp.html")
