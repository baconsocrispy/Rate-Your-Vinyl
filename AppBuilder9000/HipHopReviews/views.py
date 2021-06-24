from django.shortcuts import render, redirect
from .forms import *
from .models import *

def home(request):
    return render(request, 'HipHopReviews_home.html')

def request(request):
    form = ReviewsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("HipHopReviews_reviews")
    return render(request, 'HipHopReviews_request.html', {'form': form})

def reviews(request):
    display_reviews = Reviews.objects.all()
    context = {'display_reviews': display_reviews}
    return render(request, 'HipHopReviews_reviews.html', context)


