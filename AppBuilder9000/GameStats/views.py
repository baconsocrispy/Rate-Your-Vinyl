from django.shortcuts import render

# Create your views here.
from .forms import GamesForm, PublishersForm


def homepage(request):
    return render(request, 'GameStats/gamestats_home.html')

def addgame(request):
    form = GamesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'GameStats/gamestats_home.html')
    context = {'form': form}
    return render(request, 'GameStats/gamestats_create.html', context)

