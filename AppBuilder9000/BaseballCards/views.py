from django.shortcuts import render, redirect
from .forms import BaseballCardForm

def cards_home(request):
    return render(request, 'BaseballCards/BaseballCards_home.html')

def add_card(request):
    form = BaseballCardForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('BaseballCards_home')
    content = {'form': form}
    return render(request, 'BaseballCards/BaseballCards_add.html', content)
