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
    url = 'https://www.metacritic.com/game'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=user_agent)

    soup = BeautifulSoup(response.text, 'html.parser')
    review_dict = {'name': [], 'date': [], 'rating': []}
    context = { 'review_dict': review_dict, 'passed': False }
    for review in soup.find_all('tr'):
        if review.find("div", class_='clamp-score-wrap'):
            # had to strip everything down because websites add lots of spaces.
            # title
            review_dict['name'].append(review.find("h3").text.strip())
            # score
            review_dict['rating'].append(review.find("div", class_='clamp-score-wrap').text.strip())
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

            # Testing, if passed, will display
            # context['passed'] = True

    # the spaces before the rating and release weren't initially intended but I like them, so I'll leave them there
    for i in range(len(review_dict['name'])):
        # this line is big and scary, but not super complex
        # we use the length of one of the lists from the dict to determine how many iterations to go through
        # then we iterate through that and use the index to pull the associated name, rating, and release date
        print("Game: {}\n Rating: {}/100\n Release Date:{}\n".format(review_dict['name'][i], review_dict['rating'][i], review_dict['date'][i]))
    return render(request, 'GameStats/gamestats_topgames.html', context)