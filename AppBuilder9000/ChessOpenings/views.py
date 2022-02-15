from django.shortcuts import render, redirect
from .forms import GamesForm


def homepage(request):
    return render(request, 'ChessOpenings/chess_index.html')


def add_game(request):
    form = GamesForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            temp = form.cleaned_data.get("GamesForm.__all__")
            form.save(temp)
            return redirect(homepage)
    return render(request, "ChessOpenings/add_game.html", context)

# Create your views here.


# Create your views here.
