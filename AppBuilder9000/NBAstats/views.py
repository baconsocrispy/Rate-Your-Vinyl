from django.shortcuts import render, redirect, get_object_or_404
from .models import Defensive_Stats
from .forms import Def_Stats_Form


# Create your views here.
def nba_home(request):
    form = Def_Stats_Form(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('stats-home')
    content = {'form': form}
    return render(request, 'nba-home.html', content)


def display_all(request):
    players = Defensive_Stats.objects.all()
    content = {'players': players}
    return render(request, 'nba-display.html', content)


def show_details(request, pk):
    player = get_object_or_404(Defensive_Stats, pk=pk)
    year = player.year
    name = player.playerName
    rebs = player.defRebs
    steals = player.steals
    blocks = player.blocks

    content = {'player': player,
               'year': year,
               'playerName': name,
               'defRebs': rebs,
               'steals': steals,
               'blocks': blocks,
               }
    return render(request, 'nba-details.html', content)

""" 
def year_selected(request):
    year = request.GET['year']
    return render(request, 'nba-display.html', year)
"""





