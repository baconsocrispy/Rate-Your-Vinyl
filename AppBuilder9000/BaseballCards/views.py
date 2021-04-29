from django.shortcuts import render

def cards_home(request):
    return render(request, 'BaseballCards/BaseballCards_home.html')

