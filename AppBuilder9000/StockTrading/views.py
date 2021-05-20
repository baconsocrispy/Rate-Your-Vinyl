from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')


def stories(request):
    return render(request, 'pages/stories.html')


def about(request):
    return render(request, 'pages/about.html')

def search(request):
    return render(request, 'pages/search.html')

def results(request):
    return render(request, 'pages/results.html')

def tags(request):
    return render(request, 'pages/tags.html')

