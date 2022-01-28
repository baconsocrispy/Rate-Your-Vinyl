from django.shortcuts import render, redirect, get_object_or_404
from .form import UserForm
from .models import Profile
import requests
from bs4 import BeautifulSoup


def IceHockey_home(request):
    return render(request, 'IceHockey/IceHockey_home.html')


def IceHockey_newprofile(request):
    form = UserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('IceHockey_home')
    context = {'form': form}
    return render(request, 'IceHockey/IceHockey_newprofile.html', context)


def IceHockey_myprofile(request):
    profile_list = Profile.Profile.all()
    return render(request, 'IceHockey/IceHockey_myprofile.html', {'profile_list': profile_list})


def IceHockey_details(request, pk):
    details = get_object_or_404(Profile, pk=pk)
    context = {'details': details}
    return render(request, 'IceHockey/IceHockey_details.html', context)


def IceHockey_scrapeddata(request, pk):
    player_years = []
    player_teams = []
    player_leagues = []
    player_goals = []
    player_assists = []

    details = get_object_or_404(Profile, pk=pk)

    base_url = "https://www.eliteprospects.com/search/player?q="
    fav_name = str(details.favorite_player)
    split_name = fav_name.split()
    new_name = split_name[0] + '+' + split_name[1]
    url = base_url + new_name
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    for link in soup.find_all('a'):
        x = str(link.get('href'))
        if split_name[0].lower() and split_name[1].lower() in x:
            print(x)
            test = x.split("/")
            break

    player_id = test[4]
    player_name = test[5]

    soup2 = "https://www.eliteprospects.com/player/" + player_id + "/" + player_name
    new_result = requests.get(soup2)
    soup = BeautifulSoup(new_result.text, "html.parser")

    for goals in soup.find_all("td", class_="regular g"):
        goal = goals.string
        player_goals.append(goal)

    for assists in soup.find_all("td", class_="regular a"):
        assist = assists.string
        player_assists.append(assist)

    context = {'fav_name': fav_name, 'player_goals': player_goals, 'player_assists': player_assists, 'details': details}
    return render(request, 'IceHockey/IceHockey_scrapeddata.html', context)


def IceHockey_edit(request, pk):
    item = get_object_or_404(Profile, pk=pk)
    form = UserForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('IceHockey_myprofile')
    context = {'form': form}
    return render(request, 'IceHockey/IceHockey_edit.html', context)


def IceHockey_delete(request, pk):
    item = get_object_or_404(Profile, pk=pk)
    form = UserForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('IceHockey_myprofile')
    return render(request, 'IceHockey/IceHockey_delete.html', {'item': item, 'form': form})




