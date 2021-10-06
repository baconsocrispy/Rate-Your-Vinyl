from django.shortcuts import render, redirect
from .forms import PlayerForm


def stats_Home(request):
    return render(request, 'WarriorStats/stats_Home.html')


def add_player(request):
    form = PlayerForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('stats_Home')
    content = {'form': form}
    return render(request, 'create.html', content)
