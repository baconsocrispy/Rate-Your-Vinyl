from django.shortcuts import render, redirect
from .models import Heroes
from .forms import HeroForm


def heroability_home(request):  # calls the heroability home page when requested
    return render(request, 'HeroAbility/heroability_home.html')


def heroability_new_hero(request):
    form = HeroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('heroability_home')
    else:
        print(form.errors)
        form = HeroForm()
    context = {
        'form': form,
    }
    return render(request, 'HeroAbility/heroability_new_hero.html', context)
