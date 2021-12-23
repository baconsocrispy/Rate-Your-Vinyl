from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayersForm
from .models import Players
import requests
import json
from bs4 import BeautifulSoup


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


def player_edit(request, pk):
    item = get_object_or_404(Players, pk=pk)
    form = PlayersForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('basketball_stats_players')
    context = {'form': form}
    return render(request, 'BasketballStats/BasketballStats_edit.html', context)


def player_delete(request, pk):
    item = get_object_or_404(Players, pk=pk)
    form = PlayersForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('basketball_stats_players')
    return render(request, 'BasketballStats/BasketballStats_delete.html', {'item': item, 'form': form})


def fetch_team_name():
    full_name = {}
    url = "https://api-nba-v1.p.rapidapi.com/teams/league/standard"
    headers = {
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
        'x-rapidapi-key': "93c897feddmshe43ca8b1cec9f29p1e574bjsn0ad1ca76158a"
    }
    response = requests.request("GET", url, headers=headers)
    team_names = json.loads(response.text)
    for teams in team_names['api']['teams']:
        if teams['nbaFranchise'] == '1':
            full_name[teams['teamId']] = teams['fullName']
    return full_name


def standings_page(request):
    west_team = []
    east_team = []
    season = ' '
    if 'season' in request.POST:
        full_name_dict = fetch_team_name()
        season = request.POST['season']
        url = 'https://api-nba-v1.p.rapidapi.com/standings/standard/' + season
        headers = {
             'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
             'x-rapidapi-key': "93c897feddmshe43ca8b1cec9f29p1e574bjsn0ad1ca76158a"
        }
        response = requests.request("GET", url, headers=headers)
        team_standings = json.loads(response.text)
        for team in team_standings['api']['standings']:
            team_name = full_name_dict[team['teamId']]
            ranking = team['conference']['rank']
            team_result = (ranking, team_name)
            if team['conference']['name'] == 'west':
                west_team.append(team_result)
            else:
                east_team.append(team_result)
            west_team.sort(key=lambda a: int(a[0]))
            east_team.sort(key=lambda a: int(a[0]))
    context = {'west_team': west_team, 'east_team': east_team, 'season': season}
    return render(request, 'BasketballStats/BasketballStats_team_standings.html', context)


# This grabs a table of NBA Champions
def history_scarping(request):
    page = requests.get("https://www.dunkest.com/en/nba/news/58063/nba-champions-winners-1947-2021")
    soup = BeautifulSoup(page.content, 'html.parser')
    previous_champions = soup.find('section', class_='post__content text-article')
    champions = previous_champions.find_all(class_='wp-block-table')
    print(champions)
    return render(request, 'BasketballStats/BasketballStats_history.html')
