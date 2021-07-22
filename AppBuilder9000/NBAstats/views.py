from django.shortcuts import render, redirect, get_object_or_404
from .models import Defensive_Stats
from .forms import Def_Stats_Form
from bs4 import BeautifulSoup
import requests
from collections import OrderedDict


# RENDER HOME PAGE
def nba_home(request):
    form = Def_Stats_Form(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('stats-home')
    content = {'form': form}
    return render(request, 'nba-home.html', content)


def save_favorites(request):
    print("Hello")


# ===============================================================================================
#       Display functions to show All players, or players from specific seasons (i.e. 2020-2021)
# ===============================================================================================
def display_all(request):
    players = Defensive_Stats.objects.all()
    content = {'players': players}
    return render(request, 'nba-display.html', content)


def display_2021(request):
    year = '2020-2021'
    # Here we use Raw SQL commands to only show records from chosen year
    players = Defensive_Stats.objects.raw('SELECT * FROM NBAstats_Defensive_Stats WHERE year = %s', [year])
    content = {'players': players}
    return render(request, 'nba-display-2020-2021.html', content)


def display_2020(request):
    year = '2019-2020'
    players = Defensive_Stats.objects.raw('SELECT * FROM NBAstats_Defensive_Stats WHERE year = %s', [year])
    content = {'players': players}
    return render(request, 'nba-display-2019-2020.html', content)


def display_2019(request):
    year = '2018-2019'
    players = Defensive_Stats.objects.raw('SELECT * FROM NBAstats_Defensive_Stats WHERE year = %s', [year])
    content = {'players': players}
    return render(request, 'nba-display-2018-2019.html', content)


# ===============================================================================================
#           Display the details for individual players
# ===============================================================================================
def show_details(request, pk):
    player = get_object_or_404(Defensive_Stats, pk=pk)
    year = player.year
    name = player.playerName
    rebs = player.defRebs
    steals = player.steals
    blocks = player.blocks
    # Total Points are calculated below
    total_def_points = rebs + (steals * 3) + (blocks * 3)

    content = {'player': player,
               'year': year,
               'playerName': name,
               'defRebs': rebs,
               'steals': steals,
               'blocks': blocks,
               'total_def_points': total_def_points,
               }
    return render(request, 'nba-details.html', content)


# ===============================================================================================
#           EDIT and DELETE player functions
# ===============================================================================================
def delete_player(request, pk):
    player = get_object_or_404(Defensive_Stats, pk=pk)
    year = player.year
    form = Def_Stats_Form(data=request.POST or None, instance=player)
    if request.method == 'POST':
        player.delete()
        return redirect('display-all')
    content = {'player': player, 'year': year, 'form': form}
    return render(request, 'nba-delete.html', content)


def edit_player(request, pk):
    player = get_object_or_404(Defensive_Stats, pk=pk)
    form = Def_Stats_Form(data=request.POST or None, instance=player)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('display-all')
    content = {'form': form}
    return render(request, 'nba-edit.html', content)


# ===============================================================================================
#           Beautiful Soup
# ===============================================================================================
def b_ref(request):
    # URL page we will scrape
    brURL = "https://www.basketball-reference.com/leagues/NBA_2021_totals.html"

    page = requests.get(brURL)

    soup = BeautifulSoup(page.content, 'html.parser')
    # print([type(item) for item in list(soup.children)])

    # Get all Headers from table and put them in a list
    headers = [th.getText() for th in soup.findAll('tr', limit=1)[0].findAll('th')]
    # Select only the headers I want and put them in a list
    myHeaders = list(headers[i] for i in [1, 22, 25, 26])
    # print(myHeaders)  # This shows which headers I've selected

    # Get all table rows (tr) and put into a list.
    # Omitted row with index 0 and started at index 1 through 80
    rows = soup.findAll('tr')[1:]

    # Extract table data (td) from the rows and put into list
    allStats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]
    # This print shows how we can select a single element (allStats[row][element])
    # print(allStats[3][0])
    # print(len(allStats))
    # I could print all the players and all their stats with print(allStats)
    # But that is a lot to print to console (over 500 rows)

    # Declare empty variables to add to in the while loop
    player_dict = []  # empty list instead of dict
    check_name = ''

    for row in allStats:
        if len(row) > 0:  # check to see if list is empty
            playerName = row[0]
            defRebs = int(row[21])
            steals = int(row[24])
            blocks = int(row[25])
            total_def_points = defRebs + (steals * 3) + (blocks * 3)
            if total_def_points > 500:
                if playerName != check_name:
                    myStats = {'playerName': playerName,
                               'defRebs': defRebs,
                               'steals': steals,
                               'blocks': blocks,
                               'total_def_points': total_def_points}
                    player_dict.append(myStats)
                check_name = playerName
    context = {'player_dict': player_dict}
    return render(request, 'nba-basketball-reference.html', context)


''' My old dictionary before Mike's refactoring
    player_dict = {}
    check_name = ''
    i = 0
    keyNum = 1
    while i < len(allStats):
        # check to see if list is empty
        # sometimes an empty list is returned, which throws an error
        # this solves that issue
        if allStats[i]:  # if the list has data in it
            # Get data from allStats list and convert to type int (except for name)
            playerName = allStats[i][0]
            defRebs = int(allStats[i][21])
            steals = int(allStats[i][24])
            blocks = int(allStats[i][25])
            total_def_points = defRebs + (steals * 3) + (blocks * 3)

            if total_def_points > 500:

                # The page I'm scraping has multiple rows for a player who changed teams
                # during the season, so this if statement checks to see if I have already
                # gotten the player's total stats
                if playerName != check_name:
                    myStats = {'playerName': playerName,
                               'defRebs': defRebs,
                               'steals': steals,
                               'blocks': blocks,
                               'total_def_points': total_def_points}
                    dict_item = {'{}'.format(keyNum): myStats}
                    player_dict.update(dict_item)
                    i += 1
                    keyNum += 1  # This is the number passed to the javascript function
                else:
                    i += 1
                check_name = playerName
            else:
                i += 1
        else:
            i += 1
'''
