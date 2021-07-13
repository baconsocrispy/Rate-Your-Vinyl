from django.shortcuts import render


# Create your views here.
def nba_home(request):
    return render(request, "nba-home.html")
