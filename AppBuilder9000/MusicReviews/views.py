from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ReviewForm
from .models import Review
from bs4 import BeautifulSoup
import requests
import json


# Create your views here.


def music_reviews_home(request):
    # this will return you to the home page of music reviews
    return render(request, 'musicreviews_home.html')


def beautiful_soup(request):
    first_review = []
    page = requests.get("https://en.wikipedia.org/wiki/Music")
    soup = BeautifulSoup(page.content, 'html.parser')
    music = soup.find_all('p')
    reviews = music[0].get_text()
    print(reviews)
    return render(request, 'musicreviews_beautifulsoup.html')


def createReview(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('review_view')
    else:
        print(form.errors)
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'musicreviews_create.html', context)


def editReview(request, pk):
    item = get_object_or_404(Review, pk=pk)
    form = ReviewForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('review_view')
    return render(request, 'musicreviews_edit.html', {'item': item, 'form': form})


def review_view(request):
    reviews = Review.objects.all()
    return render(request, 'musicreviews_view.html', {'reviews': reviews})


def back_home(request):
    return render(request, '../templates/home/index.html')


def display_reviews(request, pk):
    item = get_object_or_404(Review, pk=pk)
    return render(request, 'musicreviews_viewlist.html', {'item': item})


def delete(request, pk):
    item = get_object_or_404(Review, pk=pk)
    form = ReviewForm(request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('review_view')
    context = {"item": item, "form": form}
    return render(request, "musicreviews_confirmDelete.html", context)


def confirmDelete(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('review_view')
    else:
        return redirect('review_view')

