from django.shortcuts import render, redirect,  get_object_or_404
from .models import Deck
from .forms import DeckForm

# Create your views here.
def magic_home(request):
    return render(request, 'Magic/magic_home.html')

def magic_create(request):
    form = DeckForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../browse')
    content = {'form': form}
    return render(request, 'Magic/magic_create.html', content)

def magic_browse(request):
    return render(request, 'Magic/magic_browse.html')
