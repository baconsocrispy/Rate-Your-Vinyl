from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import GamesForm, PublishersForm
from .models import Games


def homepage(request):
    return render(request, 'GameStats/gamestats_home.html')

def add_game(request):
    form = GamesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'GameStats/gamestats_home.html')
    context = {'form': form}
    return render(request, 'GameStats/gamestats_create.html', context)


def view_games(request):
    query = request.GET
    context = {}
    # for some reason .all() doesn't work here, instead we will do filter and not include anything *yet*
    # get all and return with no filtering
    game_list = Games.Game.filter()
    if query and request.method == 'GET':
        # filter if we are searching
        if query.get('search_res', None):
            game_list = Games.Game.filter(rating=query.get('search_res', None))
        elif query.get('release_year', None):
            game_list = Games.Game.filter(release_year=query.get('release_year', None))
        elif query.get('genre', None):
            game_list = Games.Game.filter(genre=query.get('genre', None))
        elif query.get('name', None):
            game_list = Games.Game.filter(name=query.get('name', None))
        # game_list = Games.Game.filter(rating=query.get('search_res', None), release_year=query.get('release_year', None),
        #                               genre=query.get('genre', None), name=query.get('name', None))

    game = request.GET.get('page', 1)
    paginator = Paginator(game_list, 10)

    try:
        game_list = paginator.page(game)
    except PageNotAnInteger:
        game_list = paginator.page(1)
    except EmptyPage:
        game_list = paginator.page(paginator.num_pages)

    context = { 'game_list': game_list }
    return render(request, 'GameStats/gamestats_all.html', context)


def game_details(request, pk):
    details = get_object_or_404(Games, pk=pk)
    context = {'details': details}
    return render(request, 'GameStats/gamestats_details.html', context)

def game_edit(request, pk):
    details = get_object_or_404(Games, pk=pk)
    form = GamesForm(data=request.POST or None, instance=details)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gamestats_viewall')
    context = {'form': form}
    return render(request, 'GameStats/gamestats_edit.html', context)


def game_delete(request, pk):
    details = get_object_or_404(Games, pk=pk)
    form = GamesForm(data=request.POST or None, instance=details)
    if request.method == 'POST':
        details.delete()
        return redirect('gamestats_viewall')
    context = { 'details': details, 'form': form }
    return render(request, 'GameStats/gamestats_delete.html', context)