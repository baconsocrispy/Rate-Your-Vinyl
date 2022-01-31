from django.shortcuts import render, redirect

from .models import Turtles


def turtles_home(request):
    form = Turtles.objects.all()
    return render(request, "Turtles/turtles_home.html")


def turtles_create(request):
    form = Turtles(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
        content = {'form': form}
        return render(request, "Turtles/turtles_create.html")
