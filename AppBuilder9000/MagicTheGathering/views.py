
from django.shortcuts import render, redirect, get_object_or_404
from .models import Collection, Card
from .forms import CardForm, CollectionForm


def MagicTheGathering_home(request):
     collection = Collection.Collection.all()
     content = {'collection': collection}
     return render(request, 'MagicTheGathering/MagicTheGathering_home.html', content)


def collection(request, pk):
     data = get_object_or_404(Collection, pk=pk)
     cards= Card.Cards.filter(card_name=pk)
     content = {'collection': data, 'cards':cards}
     return render(request, 'MagicTheGathering/ViewCollection.html', content)


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






