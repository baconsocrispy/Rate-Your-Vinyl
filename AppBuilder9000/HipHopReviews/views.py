from django.shortcuts import render, redirect, get_object_or_404
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

def artist_details(request, pk):
    details = get_object_or_404(Reviews, pk=pk)
    context = {'details': details}
    return render(request, 'HipHopReviews_details.html', context)
