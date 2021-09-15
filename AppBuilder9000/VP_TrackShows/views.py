from django.shortcuts import render


# Renders our home page
def home(request):
    return render(request, 'VP_TrackShows/home.html')


# Adds a show to our collection
def add_show(request):
    return render(request, 'VP_TrackShows/add_show.html')


# Views our shows in a table
def view_shows(request):
    return render(request, 'VP_TrackShows/view_shows.html')
