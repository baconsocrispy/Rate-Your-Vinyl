from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

def MagicTheGathering_home(request):
     # this will return user to MTG home page
     return render(request, 'MagicTheGathering/MagicTheGathering_home.html')
