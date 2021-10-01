from django.shortcuts import render


def stats_Home(request):
    return render(request, 'WarriorStats/stats_Home.html')
