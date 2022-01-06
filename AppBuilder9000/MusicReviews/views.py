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
        return redirect('review_view')
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


def back_home(request):
    return render(request, '../templates/home/index.html')


def display_reviews(request, pk):
    pk = int(pk)
    item = get_object_or_404(Review, pk=pk)
    form = ReviewForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('music_reviews_home')
        else:
            print(form.errors)
    else:
        return render(request, 'musicreviews_view.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('music_reviews_home')
    context = {"item": item, }
    return render(request, "musicreviews_confirmDelete.html", context)


def confirmDelete(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('review_view')
    else:
        return redirect('review_view')

