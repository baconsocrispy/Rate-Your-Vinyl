from django.shortcuts import render, redirect, get_object_or_404
from .models import Heroes
from .forms import HeroForm


def heroability_home(request):  # calls the heroability home page when requested
    return render(request, 'HeroAbility/heroability_home.html')


def heroability_new_hero(request):
    form = HeroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('heroability_display_all')
    else:
        print(form.errors)
        form = HeroForm()
    content = {
        'form': form,
    }
    return render(request, 'HeroAbility/heroability_new_hero.html', content)


def heroability_display_all(request):
    heroes = Heroes.heroes.all()
    content = {
        'heroes': heroes,
    }
    return render(request, 'HeroAbility/heroability_display_all.html', content)


def heroability_details(request, pk):
    pk = int(pk)
    hero = get_object_or_404(Heroes, pk=pk)
    form = HeroForm(data=request.POST or None, instance=hero)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('heroability_display_all')
        else:
            print(form.errors)
    else:
        content = {
            'form': form,
            'hero': hero,
        }
        return render(request, 'HeroAbility/heroability_details.html', content)
