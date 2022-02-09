from django.shortcuts import render, get_object_or_404, redirect


def movestate_home(request):
    return render(request, "MoveState/movestate_home.html")