from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import NovelForm
from django.contrib import messages
import requests
import http.client
import json
from .helpers import *


# the basic view when visiting the page
def home(request):
    return render(request, "Novels/Novels_home.html")


# allows new record to be created and saved to dB
def novelEntry(request):
    form = NovelForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Novels_create')
    context = {'form': form, }
    return render(request, 'Novels/Novels_create.html', context)


# displays all records
def novelDisplay(request):
    all_novels = Book.objects.all()
    return render(request, 'Novels/Novels_display.html', {'all_novels': all_novels})


# function allows all data for one record to be viewed and edited
def novelDetails(request, pk):
    pk = int(pk)
    book = get_object_or_404(Book, pk=pk)
    form = NovelForm(data=request.POST or None, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            # want to add an alert that says changes were made. This does not currently work?
            messages.info(request, 'Changes made successfully.')
            return redirect('Novels_display')
        else:
            print(form.errors)
    else:
        return render(request, 'Novels/Novels_details.html', {'form': form})


def novelDelete(request, pk):
    pk = int(pk)
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('Novels_display')
    context = {'book': book}
    return render(request, 'Novels/Novels_delete.html', context)


# =====================================================================================================
# another API test - lookup GitHub repository count by username
# mostly used just for self-learning on API response
# returns first name and number of public repositories listed on GitHub
def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'Novels/github.html', {'user': user})


# user can input a word and all definitions from API are returned
# assisted by helper function parseDefine() to iterate through dictionaries in API
def defineWord(request):
    context = {}
    if 'word' in request.GET:
        word = request.GET['word']
        url = 'https://api.dictionaryapi.dev/api/v3/entries/en_US/%s' % word
        response = requests.get(url)
        define = response.json()
        definition_list = parseDefine(define)
        print(definition_list)
        context = {'define': define, 'definition_list': definition_list}
    return render(request, 'Novels/Novels_define.html', context)






# =============================================================================================================
''' This was original API test. Not currently in use but keeping block in comment for future reference if needed
# testing API (work in progress) - this prints entire JSON response 
def defineWord(request):
    response = requests.get('https://api.dictionaryapi.dev/api/v3/entries/en_US/amazing/')
    print(response.json())
    definition = response.json()
    context = {'definitions': definition}
    return render(request, 'Novels/Novels_define.html', context)
'''