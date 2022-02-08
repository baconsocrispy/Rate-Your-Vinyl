from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayersForm
from .models import Players, Stats


# Create your views here.



def footballstatshome(request):
    return render(request, "FootballStats/Football_Stats_home.html")



def add_player_stats(request):
    form = PlayersForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('football_stats_home')
    context = {'form': form}
    return render(request, 'FootballStats/football_stats_create.html', context)



def stats(request):
    player_list = Players.Player.all()
    context = {'player_list': player_list}
    return render(request, 'FootballStats/Football_Stats_stats.html', context)


def player_details(request, pk):
    details = get_object_or_404(Players, pk=pk)
    context = {'details': details}
    return render(request, 'FootballStats/Football_Stats_details.html', context)


def player_edit(request, pk):
    item = get_object_or_404(Players, pk=pk)
    form = PlayersForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('football_stats')
    context = {'form': form}
    return render(request, 'FootballStats/Football_Stats_edit.html', context)


def player_delete(request, pk):
    item = get_object_or_404(Players, pk=pk)
    form = PlayersForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('football_stats')
    return render(request, 'FootballStats/Football_Stats_delete.html', {'item': item, 'form': form})





#Search function to be completed later
#def search(request):
    #player_list = Players.Player.all()
    #context = {'player_list': player_list}




