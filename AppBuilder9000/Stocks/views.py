from django.shortcuts import render

# Create your views here.


def stocks_home(request):
    return render(request, 'Stocks/stocks_home.html')
