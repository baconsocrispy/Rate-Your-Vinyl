from django.shortcuts import render

# Create your views here.
def footballstatshome(request):
    return render(request, "FootballStats/Football_Stats_home.html")
