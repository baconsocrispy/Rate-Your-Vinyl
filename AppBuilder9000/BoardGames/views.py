from django.shortcuts import render
from django.http import HttpResponse
#from .models import


def BoardGames_home(request):
    return render(request, 'BoardGames/BoardGames_home.html')


def BoardGames_games(request):
    return HttpResponse("This is the games list page.")


def BoardGames_addGame(request):
    return HttpResponse("This is the page to add a game.")
