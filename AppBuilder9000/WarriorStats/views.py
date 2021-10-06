from django.shortcuts import render, redirect
from .forms import PlayerForm


def stats_Home(request):
    return render(request, 'WarriorStats/stats_Home.html')


def add_player(request):
    form = PlayerForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('add_player')
    content = {'form': form}
    return render(request, 'WarriorStats/create.html', content)


def view_Player(request):
    return render(request, 'WarriorStats/players.html')
