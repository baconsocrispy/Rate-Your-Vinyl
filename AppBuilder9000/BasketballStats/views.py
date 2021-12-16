from django.shortcuts import render, redirect
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
            return redirect('basketball_stats_home')
    context = {'form': form}
    return render(request, 'BasketballStats/BasketballStats_create.html', context)
