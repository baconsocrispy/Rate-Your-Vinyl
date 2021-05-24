from django.shortcuts import render


def home(request):
    return render(request, 'StockTrade/trade_home.html')


def stories(request):
    return render(request, 'StockTrade/trade_stories.html')


def about(request):
    return render(request, 'StockTrade/trade_about.html')


def search(request):
    return render(request, 'StockTrade/trade_search.html')


def results(request):
    return render(request, 'StockTrade/trade_results.html')


def tags(request):
    return render(request, 'StockTrade/trade_tags.html')

