from django.shortcuts import render


def stock_home_page(request):
    return render(request, 'StockTracker/StockTrackerHome.html')
