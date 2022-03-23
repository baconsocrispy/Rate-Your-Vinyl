import requests
from django.shortcuts import render, redirect, get_object_or_404
from .forms import KnifeForm
from .models import ChefKnives
from bs4 import BeautifulSoup


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
    page = requests.get("http://www.cookingforengineers.com/article/39/Kitchen-Knives")
    soup = BeautifulSoup(page.content, 'html.parser')
    knives_soup = soup.findAll('div', class_='larticles')

    for i in knives_soup:
        knives.append(knives)
        zipped_list = zip(knives)
        context = {'zipped_list': zipped_list}
    return render(request, 'ChefKnives/ChefKnives_Soup.html', context)

