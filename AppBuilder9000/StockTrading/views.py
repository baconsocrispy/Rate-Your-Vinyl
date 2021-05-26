from django.shortcuts import render
from .forms import StoryForm, ResourceForm


def home(request):
    return render(request, 'StockTrade/trade_home.html')


def stories(request):
    return render(request, 'StockTrade/trade_stories.html')


def about(request):

    return render(request, 'StockTrade/trade_about.html')


def formStory(request):
    form1 = StoryForm()
    if request.method == 'POST':
        form1 = StoryForm(request.POST)
        if form1.is_valid():
            form1.save()
    context = {'form1': form1}
    return context


def formResource(request):
    form2 = ResourceForm()
    if request.method == 'POST':
        form2 = ResourceForm(request.POST)
        if form2.is_valid():
            form2.save()
    context = {'form2': form2}
    return context


def search(request):
    return render(request, 'StockTrade/trade_search.html')


def results(request):
    return render(request, 'StockTrade/trade_results.html')


def tags(request):
    return render(request, 'StockTrade/trade_tags.html')

