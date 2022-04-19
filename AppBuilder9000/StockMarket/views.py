from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm


def StockMarketHome(request):
    return render(request, 'StockMarketHome.html')


def create_account(request):
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("StockMarketHome")
    content = {'form': form}
    return render(request, 'StockMarketCreate.html', content)





