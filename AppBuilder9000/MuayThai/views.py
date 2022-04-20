from django.shortcuts import render, get_object_or_404, redirect
from .forms import FighterForm
from .models import Fighter
import requests
import json


# calls the MuayThai_home home page when requested
def Muay_Thai_Home(request):
    return render(request, 'MuayThai/MuayThai_home.html')


# calls template and accept the form inputs for adding to the db (the create part of it)
def MuayThai_fighter_entry(request):
    form = FighterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MuayThai_display_fighters')
    else:
        print(form.errors)
        form = FighterForm()
    content = {
        'form': form,
    }
    return render(request, 'MuayThai/MuayThai_fighter_entry.html', content)


# Display fighter's names
def MuayThai_display_fighters(request):
    fighters = Fighter.Fighter.all()
    content = {
        'fighters': fighters,
    }
    return render(request, 'MuayThai/MuayThai_display_fighters.html', content)


# call the details template
def MuayThai_fighters_details(request, pk):
    pk = int(pk)
    fighter = get_object_or_404(Fighter, pk=pk)
    form = FighterForm(data=request.POST or None, instance=fighter)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('MuayThai_display_fighters')
        else:
            print(form.errors)

    else:
        content = {
            'form': form,
            'fighter': fighter,
        }
        return render(request, 'MuayThai/MuayThai_fighters_details.html', content)


# function to we are deleting from the database
def MuayThai_delete_fighter(request, pk):
    pk = int(pk)
    fighter = get_object_or_404(Fighter, pk=pk)
    if request.method == 'POST':
        fighter.delete()
        return redirect('MuayThai_display_fighters')
    content = {
        "fighter": fighter,
    }
    return render(request, "MuayThai/MuayThai_delete.html", content)


# function used to confirm the delete action
def MuayThai_delete(request):
    if request.method == 'POST':
        form = FighterForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('MuayThai_display_fighters')
    else:
        return redirect('MuayThai_display_fighters')



    ######## API code section
def MuayThai_bets_api(request):
    weight = []
    fighter_rank = []
    fighter_name = []

    ### Code snippet (python requests)
    url = "https://current-ufc-rankings.p.rapidapi.com/"

    headers = {
        "X-RapidAPI-Host": "current-ufc-rankings.p.rapidapi.com",
        "X-RapidAPI-Key": "e62380c195msh635581688557802p1f24ebjsnf7d94c60773c"
    }

    response = requests.request("GET", url, headers=headers)
    ### END Code snippet (python requests)

    fight_rankings = json.loads(response.text)  # It returns a Python object.
    for i in fight_rankings:  # 'i' is the variable in fight_rankings
        weight_class = i['weightClass']
        weight.append(weight_class)
        fighters = i['fighters']
        for j in fighters:  # 'j' is the variable in fighters
            rankings = j['fighter_ranking']
            fighter_rank.append(rankings)
            names = j['fullName']
            fighter_name.append(names)

    # prints out variables
    print(weight)
    print(fighter_rank)
    print(fighter_name)


    return render(request, 'MuayThai/MuayThai_bets_api.html')
