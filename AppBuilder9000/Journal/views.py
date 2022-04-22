from django.shortcuts import render, redirect,  get_object_or_404
from .models import Entry
from .forms import EntryForm
import requests
import json
from bs4 import BeautifulSoup


def journal_home(request):
    return render(request, 'Journal/journal_home.html')


def journal_create(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../read')
    content = {'form': form}
    return render(request, 'Journal/journal_create.html', content)


def journal_read(request):
    entry = Entry.Entries.all()
    content = {'entry': entry}
    return render(request, 'Journal/journal_read.html', content)


def journal_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    form = EntryForm(data=request.POST or None, instance=entry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../../read')
    content = {'form': form, 'entry': entry}
    return render(request, 'Journal/journal_update.html', content)


def journal_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('../../read')
    content = {'entry': entry}
    return render(request, 'Journal/journal_delete.html', content)


def journal_api(request):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": "portland", "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com",
        "X-RapidAPI-Key": "aa3d3af1d8mshe07b323c70b5c20p174de6jsn68e2b0bf2a3b"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    api_info = json.loads(response.text)
    current_temperature = str(api_info["current_observation"]["condition"]["temperature"]) + ' \N{DEGREE SIGN}F'
    content = {"current_temperature": current_temperature}
    return render(request, 'Journal/journal_api.html', content)


def journal_bs(request):
    page = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup)
    content = {"soup": soup}
    return render(request, 'Journal/journal_bs.html', content)
