from django.shortcuts import render, redirect, get_object_or_404
import requests
from .forms import QuoteForm
# Create your views here.
def home(request):
    return render(request, 'Quotes/Quotes_home.html',)

def Quotes_add(request):
    form = QuoteForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Quotes_add')
    return render(request, 'Quotes/Quotes_add.html', {'form': form})