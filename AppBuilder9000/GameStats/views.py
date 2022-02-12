from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import GamesForm, PublishersForm
from .models import Games
import requests
from bs4 import BeautifulSoup


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


def top_games(request):
    review_dict = scrape_site()

    name = review_dict['name']
    date = review_dict['date']
    rating = review_dict['rating']
    gameId = review_dict['id']
    test = zip(name, date, rating, gameId)
    context = {'data': test, 'passed': False}
    return render(request, 'GameStats/gamestats_topgames.html', context)


def top_game_one(request, id):
    review_dict = scrape_site()

    context = {'name': review_dict['name'][id], 'date': review_dict['date'][id], 'rating': review_dict['rating'][id],
               'image': review_dict['image'][id], 'summary': review_dict['summary'][id] }
    return render(request, 'GameStats/gamestats_view_one.html', context)

def scrape_site():
    url = 'https://www.metacritic.com/game'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=user_agent)

    soup = BeautifulSoup(response.text, 'html.parser')
    review_dict = {'name': [], 'date': [], 'rating': [], 'image': [], 'summary': [], 'id': []}

    tempID = 0
    for review in soup.find_all('tr'):
        if review.find("div", class_='clamp-score-wrap'):
            # had to strip everything down because websites add lots of spaces.
            # title
            review_dict['name'].append(review.find("h3").text.strip())
            # score
            review_dict['rating'].append(review.find("div", class_='clamp-score-wrap').text.strip())
            # image URL
            review_dict['image'].append(review.find("img")["src"])
            # summary
            review_dict['summary'].append(review.find(class_="summary").text.strip())

            # release date
            a = review.find_all(class_="clamp-details")
            for element in a:
                try:
                    # print(element.find("span").text.strip())
                    # in the event we come up with something other than a normal string, .text.strip() won't work
                    # thus cleaning invalid inputs, and we just don't add to the dict if they are invalid
                    review_dict['date'].append(element.find("span").text.strip())
                except AttributeError:
                    pass
            review_dict['id'].append(tempID)
            tempID += 1
    return review_dict