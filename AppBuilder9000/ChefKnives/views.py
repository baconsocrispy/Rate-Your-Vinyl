from bs4 import BeautifulSoup
from django.shortcuts import render, redirect, get_object_or_404
import requests
from .forms import KnifeForm
from .models import ChefKnives
import unicodedata


# Create your views here.

def home(request):
    return render(request, 'ChefKnives/ChefKnives_Home.html')


def chefknives_view(request):
    view = ChefKnives.objects.all()
    return render(request, 'ChefKnives/ChefKnives_View.html', {'view': view})


def chefknives_create(request):
    form = KnifeForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ChefKnives_Create')
        else:
            print(form.errors)
            form = KnifeForm()
    context = {'form': form}
    return render(request, 'ChefKnives/ChefKnives_Create.html', context)


def chefknives_details(request, pk):
    details = get_object_or_404(ChefKnives, pk=pk)
    context = {'details': details}
    return render(request, "ChefKnives/ChefKnives_Details.html", context)


def chefknives_edit(request, pk):
    obj = get_object_or_404(ChefKnives, pk=pk)
    form = KnifeForm(data=request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('ChefKnives_View')
    else:
        return render(request, "ChefKnives/ChefKnives_Edit.html", {'form': form})


def chefknives_delete(request, pk):
    obj = get_object_or_404(ChefKnives, pk=pk)
    form = KnifeForm(data=request.POST or None, instance=obj)
    if request.method == 'POST':
        obj.delete()
        return redirect('ChefKnives_View')
    context = {
        "object": obj
    }
    return render(request, "ChefKnives/ChefKnives_Delete.html", context)


def chefknives_soup(request):
    knives = []

    page = requests.get("https://www.cnet.com/home/kitchen-and-household/best-chef-knife-for-2022/")
    soup = BeautifulSoup(page.content, 'html.parser')
    knives_soup = soup.find('div', class_='col-7 article-main-body row')
    knife = knives_soup.find_all('div', class_='shortcode listicle')

    for i in knife:
        knifes = i.find('p')
        chef = knifes.text.strip()
        knives.append(chef)

    print(knives)

    context = {'knives': knives}
    return render(request, 'ChefKnives/ChefKnives_Soup.html', context)

