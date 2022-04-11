from django.shortcuts import render, redirect
from .forms import CharacterForm, SeriesForm
from .models import Characters
import requests
import json

# Create your views here.
def home(request):
    return render(request,
    'FictionalCharacters/FictionalCharacters_Home.html')

# Create a function to add a series to dB
def series_create(request):
    form = SeriesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('FictionalCharacters_CreateSeries')
        else:
            print(form.errors)
            form = SeriesForm()
    context = {'form': form}
    return render(request,
    'FictionalCharacters/FictionalCharacters_CreateSeries.html', context)

# Create a function to add a character to dB
def characters_create(request):
    form = CharacterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('FictionalCharacters_Create')
        else:
            print(form.errors)
            form = CharacterForm()
    context = {'form': form}
    return render(request,
    'FictionalCharacters/FictionalCharacters_Create.html', context)

# Create a function to list entries in Characters dB
def list_characters(request):
    # Retrieves all entries from dB in alphabetical order by name
    char_sort = Characters.objects.order_by('name')
    return render(request,
    'FictionalCharacters/FictionalCharacters_View.html', {'chars': char_sort})

# Create a function to list search results of Characters dB
def search_characters(request):
    if request.method == "POST":
        searched = request.POST['searched']
        chars = Characters.objects.filter(name__contains=searched)
        return render(request,
        'FictionalCharacters/FictionalCharacters_Search.html', {'searched': searched, 'chars': chars})
    else:
        return render(request,
        'FictionalCharacters/FictionalCharacters_Search.html', {})

# Create a function to return character info based on primary key ID
def show_char(request, char_id):
    char = Characters.objects.get(pk=char_id)
    return render(request,
    'FictionalCharacters/FictionalCharacters_ShowChar.html', {'char': char})

# Create a function to allow and accept valid edits to the dB records
def edit_char(request, char_id):
    char = Characters.objects.get(pk=char_id)
    form = CharacterForm(request.POST or None, instance=char)
    if form.is_valid():
        form.save()
        return redirect('FictionalCharacters_View')
    return render(request,
    'FictionalCharacters/FictionalCharacters_Edit.html', {'char': char, 'form': form})

# Create a function to delete records from dB
def delete_char(request, char_id):
    char = Characters.objects.get(pk=char_id)
    char.delete()
    return redirect('FictionalCharacters_View')


####### API CODE #######
"""
API will allow users to enter names of two characters they 'ship', and will return a
calculation of how likely the relationship will succeed. Just for entertainment purposes.
"""

def fc_calc(request):
    try:
        if request.method == 'POST':
            f = request.POST.get('fname')
            s = request.POST.get('sname')
            res = fc_api(f,s)
            context = {
                'fname': res['fname'],
                'sname': res['sname'],
                'percent': int(res['percentage']),
                'result': res['result'],
            }
            return render(request, 'FictionalCharacters/FictionalCharacters_Results.html',context={'data':context})
        return render(request,'FictionalCharacters/FictionalCharacters_API.html')
    except:
        return render(request, 'FictionalCharacters/FictionalCharacters_Error.html')

def fc_api(f, s):
    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"sname": s, "fname": f}

    headers = {
        "X-RapidAPI-Host": "love-calculator.p.rapidapi.com",
        "X-RapidAPI-Key": "97d934559cmshcc7dd84616b2d90p107d36jsn5b9a1d832d36"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    test = json.loads(response.text)
    print(response.text)

    return test