from django.shortcuts import render, redirect, get_object_or_404
import requests
import json


# Create your views here.


def music_reviews_home(request):
    # this will return you to the home page of music reviews
    return render(request, 'musicreviews_home.html')
