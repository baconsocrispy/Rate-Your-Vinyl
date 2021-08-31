from django.shortcuts import render

# Displays the home page
def BestGamesEver_Home(request):
    return render(request, 'BestGamesEver/home.html')
