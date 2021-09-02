from django.shortcuts import render, redirect
from .forms import PlayerForm
from .models import Player

# Displays Home Page



def blazerstats_home(request):
    return render(request, 'BlazerStats/home.html')


def blazerstats_create(request):
    form = PlayerForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("blazerstats_create")

    return render(request, 'BlazerStats/Blazercreate.html', {"form":form})


def blazerstats_players(request):
    player_list = Player.objects.all()
    return render(request, 'BlazerStats/Players.html', {'player_list': player_list})


def blazerstats_details(request, pk):
    details = Player.objects.get(pk=pk)
    return render(request, 'BlazerStats/details.html', {'details': details})