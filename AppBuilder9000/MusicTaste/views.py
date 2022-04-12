from django.shortcuts import render, get_object_or_404, redirect
import requests
import json
from bs4 import BeautifulSoup


def musictaste_home(request):
    return render(request, "MusicTaste/MusicTaste_home.html")
