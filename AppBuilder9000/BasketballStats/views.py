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
def history_scraping(request):
    champion_list = []
    page = requests.get("https://www.dunkest.com/en/nba/news/58063/nba-champions-winners-1947-2021")
    soup = BeautifulSoup(page.content, 'html.parser')
    previous_champions = soup.find('section', class_='post__content text-article')
    champions = previous_champions.find_all('tr')[1:]
    for tr in champions:
        td = tr.find_all('td')
        row = [i.text for i in td]
        cells = row
        champion_list.append(cells)
    context = {'champion_list': champion_list}
    return render(request, 'BasketballStats/BasketballStats_history.html', context)


def web_scraping(request):
    player_numbers = []
    roster = []
    position = []
    height = []
    weight = []
    birthday = []
    years_experience = []
    college = []
    page = requests.get("https://www.basketball-reference.com/teams/POR/2022.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', id='roster')
    one = table.find('tbody')
    two = one.find_all('th')
    for i in two:
        three = i.text
        player_numbers.append(three)

    four = one.find_all('tr')
    for tds in four:
        td_list = tds.find_all('td')

        name_list = td_list[0]
        names = name_list.text
        roster.append(names)

        pos_list = td_list[1]
        pos = pos_list.text
        position.append(pos)

        height_list = td_list[2]
        heights = height_list.text
        height.append(heights)

        weight_list = td_list[3]
        weights = weight_list.text
        weight.append(weights)

        bday_list = td_list[4]
        bdays = bday_list.text
        birthday.append(bdays)

        experience_list = td_list[6]
        exp = experience_list.text
        years_experience.append(exp)

        college_list = td_list[7]
        colleges = college_list.text
        college.append(colleges)

    zipped_list = zip(player_numbers, roster, position, height, weight, birthday, years_experience, college)
    context = {
        'zipped_list': zipped_list
    }
    return render(request, 'BasketballStats/BasketballStats_web_scraping.html', context)


def ball_dont_lie(request):
    atlantic = []
    central = []
    southeast = []
    northwest = []
    pacific = []
    southwest = []
    utah_teams = []
    atlantic_logos = []
    central_logos = []
    southeast_logos = []
    northwest_logos = []
    pacific_logos = []
    southwest_logos = []
    url = "https://api-nba-v1.p.rapidapi.com/teams/league/standard"

    headers = {
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
        'x-rapidapi-key': "93c897feddmshe43ca8b1cec9f29p1e574bjsn0ad1ca76158a"
    }

    response = requests.request("GET", url, headers=headers)
    teams_info = json.loads(response.text)
    team_list = teams_info['api']['teams']
    for teams in team_list:
        name = teams['fullName']
        logo = teams['logo']
        division = teams['leagues']['standard']['divName']

        if division == 'Atlantic':
            atlantic.append(name)
            atlantic_logos.append(logo)

        elif division == 'Central':
            central.append(name)
            central_logos.append(logo)

        elif division == 'Southeast':
            southeast.append(name)
            southeast_logos.append(logo)

        elif division == 'Northwest':
            if name == 'Utah Blue':
                utah_teams.append(name)
            elif name == 'Utah White':
                utah_teams.append(name)
            else:
                northwest.append(name)
                northwest_logos.append(logo)

        elif division == 'Pacific':
            pacific.append(name)
            pacific_logos.append(logo)

        elif division == 'Southwest':
            southwest.append(name)
            southwest_logos.append(logo)

    eastern_conference = zip(atlantic, central, southeast)
    western_conference = zip(northwest, pacific, southwest)
    context = {
        'eastern_conference': eastern_conference, 'western_conference': western_conference,
        'atlantic': atlantic, 'central': central, 'southeast': southeast,
        'northwest': northwest, 'pacific': pacific, 'southwest': southwest,
        'atlantic_logos': atlantic_logos, 'central_logos': central_logos, 'southeast_logos': southeast_logos,
        'northwest_logos': northwest_logos, 'pacific_logos': pacific_logos, 'southwest_logos': southwest_logos
    }
    return render(request, 'BasketballStats/BasketballStats_bdl_api.html', context)


def save_favorites(request):
    teams = []
    conferences = []
    divisions = []
    url = "https://www.balldontlie.io/api/v1/teams"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    team_list = data['data']
    for i in team_list:
        team_name = i['full_name']
        conference = i['conference']
        division = i['division']
        teams.append(team_name)
        conferences.append(conference)
        divisions.append(division)
    team_info = zip(teams, conferences, divisions)
    print(team_info)
    return render(request, 'BasketballStats/BasketballStats_save_api.html')
