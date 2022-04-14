from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
import requests
import json
from bs4 import BeautifulSoup


def musictaste_home(request):
    return render(request, "MusicTaste/MusicTaste_home.html")


def test(request):
    return render(request, "MusicTaste/test.html")


def registerform(request):
    form = UserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MusicTaste_home')
    context = {'form': form}
    return render(request, 'MusicTaste/test.html', context)
