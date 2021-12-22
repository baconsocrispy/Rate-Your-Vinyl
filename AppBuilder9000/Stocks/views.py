
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Stocks
from .forms import StocksForm

# Create your views here.


def stocks_home(request):
    return render(request, 'Stocks/stocks_home.html')


def favorites(request):
    stocks = Stocks.objects.all()
    return render(request, 'Stocks/stocks_favorites.html', {'stocks': stocks})


def add_favorites(request):
    form = StocksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('stocks_favorites')
    else:
        print(form.errors)
        form = StocksForm()
    context = {
        'form': form,
    }
    return render(request, 'Stocks/stocks_add_favorites.html', context)


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Stocks, pk=pk)
    return render(request, 'Stocks/stocks_details.html', {'item': item})

