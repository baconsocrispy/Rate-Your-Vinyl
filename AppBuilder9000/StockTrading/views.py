from django.shortcuts import render, redirect
from .models import Story, Resource
from .forms import StoryForm, ResourceForm


def home(request):
    return render(request, 'StockTrade/trade_home.html')


def stories(request):
    cards = Story.Stories.all()
    context = {'cards': cards}
    return render(request, 'StockTrade/trade_stories.html', context)


def about(request):
    form1 = StoryForm()
    form2 = ResourceForm()

    # if request.method == 'POST':
    #     form2 = ResourceForm(request.POST)
    #     if form2.is_valid():
    #         form2.save()
    #
    # if request.method == 'POST':
    #     form1 = StoryForm(request.POST)
    #     if form1.is_valid():
    #         form1.save()

    context = {'form1': form1, 'form2': form2}
    return render(request, 'StockTrade/trade_about.html', context)


def story(request):
    if request.method == 'POST':
        form1 = StoryForm(request.POST)
        if form1.is_valid():
            form1.save()
    response = redirect('about')
    return response


def resource(request):
    if request.method == 'POST':
        form2 = ResourceForm(request.POST)
        if form2.is_valid():
            form2.save()
    response = redirect('about')
    return response


def search(request):
    return render(request, 'StockTrade/trade_search.html')


def results(request):
    return render(request, 'StockTrade/trade_results.html')


def tags(request):
    return render(request, 'StockTrade/trade_tags.html')

