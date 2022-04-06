from django.shortcuts import render


def heroability_home(request):  # calls the heroability home page when requested
    return render(request, 'HeroAbility/heroability_home.html')
