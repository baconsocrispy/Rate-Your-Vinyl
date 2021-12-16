from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayersForm
from .models import Players


# Create your views here.
def home(request):
    return render(request, 'BasketballStats/BasketballStats_home.html')


def create_player(request):
    form = PlayersForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('basketball_stats_players')
    context = {'form': form}
    return render(request, 'BasketballStats/BasketballStats_create.html', context)


def player_stats(request):
    player_list = Players.Player.all()
    context = {'player_list': player_list}
    return render(request, 'BasketballStats/BasketballStats_players.html', context)


def player_details(request, pk):
    details = get_object_or_404(Players, pk=pk)
    context = {'details': details}
    return render(request, 'BasketballStats/BasketballStats_details.html', context)
