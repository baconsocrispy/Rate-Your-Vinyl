from django.shortcuts import render

def home(request):
    return render(request, 'HipHopReviews_home.html')
