from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import SpeedrunForm
from .game_forms import GameForm
from .models import Record, GameName


# render home page
def speed_run_home(request):
    return render(request, "speed_run_home.html")


# create speedrun record form using model form in django
def add_record(request):
    form = SpeedrunForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('speed_run_home')
    else:
        print(form.errors)
        form = SpeedrunForm()
        context = {'form': form}
    return render(request, 'speed_run_create.html', context)


# create game form using model form in django
def add_game(request):
    form = GameForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('speed_run_create')
    else:
        print(form.errors)
        form = GameForm()
        context = {'form': form}
    return render(request, 'speed_run_create_game.html', context)


# displays a list of all games entered as GameName Objects
def all_games(request):
    games = GameName.objects.all()
    return render(request, 'speed_run_all_games.html', {'games': games})


# passes Record information if player has a record for the selected game
def game_record(request, pk):
    gamename = get_object_or_404(GameName, pk=pk)
    records = Record.objects.filter(game=gamename).order_by("time")
    content = {'gamename': gamename, 'records': records}
    return render(request, 'speed_run_game_records.html', content)


# displays all details relevant to a selected player
def speed_run_details(request, pk):
    details = get_object_or_404(Record, pk=pk)
    content = {'details': details}
    return render(request, 'speed_run_details.html', content)


# allows the user to edit an entry
def speed_run_edit(request, pk):
    item = get_object_or_404(Record, pk=pk)
    form = SpeedrunForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('speed_run_all_games')
        else:
            print(form.errors)
    else:
        return render(request, 'speed_run_edit.html', {'form': form, 'item': item})


# allows users to delete a record
def speed_run_delete(request, pk):
    item = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('speed_run_all_games')
    context = {'item': item}
    return render(request, 'speed_run_delete.html', context)

