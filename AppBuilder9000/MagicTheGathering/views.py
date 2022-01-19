from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Collection, Card
from .forms import CardForm, CollectionForm

def MagicTheGathering_home(request):
     # this will return user to MTG home page
     return render(request, 'MagicTheGathering/MagicTheGathering_home.html')



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
