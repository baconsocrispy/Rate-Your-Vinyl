from django.shortcuts import render, redirect, get_object_or_404
from .models import Heroes
from .forms import HeroForm


# calls the heroability home page when requested
def heroability_home(request):
    return render(request, 'HeroAbility/heroability_home.html')


# call template and accept the form inputs for adding to the db
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


# call all records and the display template
def heroability_display_all(request):
    heroes = Heroes.heroes.all()
    content = {
        'heroes': heroes,
    }
    return render(request, 'HeroAbility/heroability_display_all.html', content)


# call the details template
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
