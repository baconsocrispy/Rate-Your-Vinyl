
from django.shortcuts import render, redirect
from .forms import PlayerForm, TeamForm
from django.contrib import messages
from .models import Player, Team


# Create your views here.
def StatCheckHome(request):
    return render(request,'StatCheck/StatCheckHOME.html')

def CheckPlayer(request):
    if request.method == "POST":
        playerForm = PlayerForm(request.POST, request.FILES)
        if playerForm.is_valid():
            playerForm.save()
            messages.success(request, ('Your player was successfully added!'))
        else:
            messages.error(request, 'Error saving form')


        return redirect("StatCheckPLAYER")
    playerForm = PlayerForm()
    Stat = Player.objects.all()
    return render(request, "StatCheck/StatCheckPLAYER.html", context={'playerForm':playerForm, 'Stat':Stat})

def CheckTeam(request):
    if request.method == "POST":
        teamForm = TeamForm(request.POST, request.FILES)
        if teamForm.is_valid():
            teamForm.save()
            messages.success(request, ('Your team was successfully added!'))
        else:
            messages.error(request, 'Error saving form')


        return redirect("StatCheckTEAM")
    teamForm = TeamForm()
    Stat = Team.objects.all()
    return render(request, "StatCheck/StatCheckTEAM.html", context={'teamForm':teamForm, 'Stat':Stat})