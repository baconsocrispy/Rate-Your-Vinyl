from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ReviewForm
from .models import Review
import requests
import json


# Create your views here.


def music_reviews_home(request):
    # this will return you to the home page of music reviews
    return render(request, 'musicreviews_home.html')


def createReview(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('music_reviews_home')
    else:
        print(form.errors)
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'musicreviews_create.html', context)


def review_view(request):
    reviews = Review.objects.all()
    return render(request, 'musicreviews_view.html', {'reviews': reviews})
