from django.shortcuts import render, redirect
from .forms import PlayerForm


# Displays Home Page
from .models import Player


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
    list_content = {'player_list': player_list}
    return render(request, 'BlazerStats/Players.html', list_content)
