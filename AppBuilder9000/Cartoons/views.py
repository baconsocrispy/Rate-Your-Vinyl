from django.shortcuts import render, redirect, get_object_or_404
from .forms import CartoonForm
from .models import Cartoon, Definition
import requests
from bs4 import BeautifulSoup
import json

# Create your views here.
""" HOME, CREATE, DISPLAY, UPDATE, DELETE CARTOON SECTION """
def Cartoons(request):
    return render(request, 'Cartoons/Cartoons_home.html')

def CreateCartoon(request):
    form = CartoonForm(data=request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('Cartoons_home')
    context = {'form': form}
    return render(request, "Cartoons/Cartoons_create.html", context)

def DisplayCartoons(request):
    cartoon_list = Cartoon.Cartoons.all().order_by("premier_date")
    context = {'cartoon_list': cartoon_list}
    return render(request, 'Cartoons/Cartoons_list.html', context)

def DisplayDetails(request, pk):
    item = get_object_or_404(Cartoon, pk=pk)
    context = {'item': item}
    return render(request, 'Cartoons/Cartoons_details.html', context)

def DeleteItem(request, pk):
    context = {}
    item = get_object_or_404(Cartoon, pk=pk)

    if request.method == "POST":
        item.delete()
        return redirect("Cartoons_list")

    return render(request, "Cartoons/Cartoons_delete.html", context)

def UpdateItem(request, pk):
    item = Cartoon.Cartoons.get(pk=pk)
    form = CartoonForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('Cartoons_list')

    context = {'item': item, 'form': form}
    return render(request, 'Cartoons/Cartoons_up_date.html', context)

""" BEAUTIFULSOUP SECTION """
def RankingScrape(request):
    # create empty list
    top_cartoons = []
    # set up BeautifulSoup
    source = requests.get("https://www.indiewire.com/feature/best-animated-series-all-time-cartoons-anime-tv-1202021835/5/")
    bs = BeautifulSoup(source.content, 'html.parser')
    # Get all the h3 tags under the div 'entry-content' from source site
    rankings = bs.find('div', class_='entry-content')
    rank = rankings.find_all('h3')
    # for loop through the h3 tags but in reverse order (because they are displayed reversed on the source page)
    for i in reversed(rank):
        titles = i.text
        top_cartoons.append(titles)
    # delete indexes 8-9 which are irrelevant h3 tags
    del top_cartoons[8:10]
    # console test
    print(top_cartoons)

    context = {'top_cartoons': top_cartoons}
    return render(request, 'Cartoons/Cartoons_rankings.html', context)

""" OXFORD API SECTION """
def OxfordAPI(request):
    # set up api connection
    app_id='591386c7'
    app_key='ea768fd0e3d3a96ec8b39d08533c1f36'
    language='en-us'
    fields ='definitions'
    strictMatch ='false'
    # create empty list
    definition=[]
    if request.method=='POST':
        value=request.POST['word_id'].lower()
        # if input is blank it will display this message
        if value=="":
            messages.info(request, 'Please enter a search term')
        else:
            url ='https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + value + '?fields=' + fields + '&strictMatch=' + strictMatch;
            info=requests.get(url,headers={'app_id':app_id, 'app_key':app_key})
            oxford_info=info.json()
            result=oxford_info['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
            definition.append(result)

            save_definition = Definition.Definitions.create(
                value=value,
                definition=definition
            )
            save_definition.save()

        context={'value':value,'definition':definition}
        # if input is not blank then it will return the context
        return render(request, 'Cartoons/Cartoons_api.html', context)
    else:
        return render(request, 'Cartoons/Cartoons_api.html')


def DisplayDefinitions(request):
    definition_list = Definition.Definitions.all().order_by("value")
    context = {'definition_list': definition_list}
    return render(request, 'Cartoons/Cartoons_definitions.html', context)


