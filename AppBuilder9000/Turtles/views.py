from django.shortcuts import render


def turtles_home(request):
    return render(request, "Turtles/turtles_home.html")
