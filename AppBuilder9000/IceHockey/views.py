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

def IceHockey_scrapedata(request):
    player_years = []
    player_teams = []
    player_leagues = []
    player_goals = []
    player_assist = []

    base_url = "https://www.eliteprospects.com/search/player?q="
    fav_name = Profile.favorite_player
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
        player_assist.append(assist)




    return render(request, 'IceHockey/IceHockey_details.html', context)




