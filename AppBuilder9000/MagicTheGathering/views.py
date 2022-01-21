import json
import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Collection, Card
from .forms import CardForm, CollectionForm
from mtgsdk import Card, Set, Type, Supertype, Subtype, Changelog


def MagicTheGathering_home(request):
     #collection = Collection.Collection.all()
     #content = {'collection': collection}
     return render(request, 'MagicTheGathering/MagicTheGathering_home.html')


def collection(request):
     cards = Card.Cards.all()
     context = {'cards': cards}
     return render(request, 'MagicTheGathering/ViewCollection.html', context)


def create_collection(request):
     form = CollectionForm(data=request.POST or None)
     if request.method == 'POST':
          if form.is_valid():
               form.save()
               return redirect('create')
     content = {'form': form}
     return  render(request, 'MagicTheGathering/CreateNewCollection.html', content)

def create_card(request):
     form = CardForm(data=request.POST or None)
     if request.method == 'POST':
          if form.is_valid():
               form.save()
     content = {'form': form}
     return render(request, 'MagicTheGathering/AddCardTransaction.html', content)

def details(request, pk):
     card_details = get_object_or_404(Card, pk=pk)
     context = {'card_details':card_details}
     return render(request, 'MagicTheGathering/CardDetails.html', context)


def editCardInfo(request, pk):
    card_details = get_object_or_404(Card, pk=pk)
    form = CardForm(data=request.POST or None, instance=card_details)
    if request.method == 'POST':
         if form.is_valid():
              form.save()
              return redirect('collection')
         else:
              print(form.errors)
    return render(request, 'MagicTheGathering/CardEdit.html', {'form': form})

def delete_card(request, pk):
    item = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('collection')
    context = {"item": item,}
    return render(request, "MagicTheGathering/Magic_confirmdelete.html", context)

def MagicTheGathering_API(request):
    url = "https://api.magicthegathering.io/v1/cards"

    parameters = {
        'name':'Tarmogoyf'
    }

    response = requests.get(url, params=parameters)
    data = json.loads(response.text)
    card_info = data['cards']
    cards=card_info[0]
    name=cards['name']
    type=cards['type']
    color=cards['colors']
    manaCost=cards['manaCost']
    text=cards['text']
    print(type)
    print(color)
    print(manaCost)
    print(name)
    print(text)
    return render(request, 'MagicTheGathering/Magic_API.html')








