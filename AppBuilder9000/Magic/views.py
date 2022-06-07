from django.shortcuts import render, redirect,  get_object_or_404
from .models import Deck
from .forms import DeckForm

#Story 1: Build the basic app
def magic_home(request):
    return render(request, 'Magic/magic_home.html')


#Story 2: Create a model
def magic_create(request):
    form = DeckForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../browse')
    content = {'form': form}
    return render(request, 'Magic/magic_create.html', content)

#Story 3: Display items from database
def magic_browse(request):
    deck = Deck.Deck.all()
    content = {
        'deck': deck,
    }
    return render(request, 'Magic/magic_browse.html', content)

