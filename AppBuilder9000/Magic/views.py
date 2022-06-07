from django.shortcuts import render, redirect,  get_object_or_404
from .models import Deck, Comment
from .forms import DeckForm, CommentForm

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


#Story 4: Details Page
def magic_details(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    form = CommentForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../details')
    comment = Comment.Comments.all()
    content = {
        'deck': deck,
        'comment': comment,
        'form': form,
    }
    return render(request, 'Magic/magic_details.html', content)
