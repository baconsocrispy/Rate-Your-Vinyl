from django.shortcuts import render


# Story #1: Build the basic app ----------------------------------------------------------------------------------------

def texmex_home(request):
    return render(request, 'TexMex/texmex_home.html')
# Create your views here.
