from django.shortcuts import render, redirect
from .forms import PlayerForm
from .models import Player

# Displays Home Page



def BlazerStats_Home(request):
    return render(request, 'BlazerStats/home.html')


def BlazerStats_Create(request):
    form = PlayerForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("BlazerStats_Create")

    return render(request, 'BlazerStats/Blazercreate.html', {"form":form})


def BlazerStats_Players(request):
    player_list = Player.objects.all()
    return render(request, 'BlazerStats/Players.html', player_list)
        {'player_list': player_list}