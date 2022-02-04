from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from .forms import ComposerForm
from .models import Composer
import requests
from bs4 import BeautifulSoup


# Create your views here.
def composers(request):
    return render(request, 'Composers/composers_home.html')


def create_composer(request):
    form = ComposerForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('composers_home')
    content = {'form': form}
    return render(request, 'Composers/composers_create.html', content)


def composers_list(request):
    composer_list = Composer.Composers.all()
    context = {'composer_list': composer_list}
    return render(request, 'Composers/composers_list.html', context)


def composers_details(request,pk):
    details = get_object_or_404(Composer, pk=pk)
    context = {'details': details}
    return render(request, 'Composers/composers_details.html', context)


def composers_edit(request, pk):
    item = get_object_or_404(Composer, pk=pk)
    form = ComposerForm(request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('composers_list')
    context = {'form': form}
    return render(request, 'Composers/composers_edit.html', context)

def composers_delete(request, pk):
    item = get_object_or_404(Composer, pk=pk)
    form = ComposerForm(request.POST or None, instance=item)
    if request.method == 'POST':
            item.delete()
            return redirect('composers_list')
    return render(request, 'Composers/composers_delete.html', {'item': item, 'form': form})


"""List of the top 25 composers according to this site"""
def composer_scraping2(request):
    top20composers=[]
    page = requests.get('https://www.thetoptens.com/greatest-classical-composers/')
    soup = BeautifulSoup(page.content, 'html.parser')
    composers_soup = soup.find_all('b')
    for i in composers_soup:
        if i != 'hublink':
            composers = i.text
            top20composers.append(composers)
            print(composers)
    return render(request, 'Composers/top100_composers.html')


def composer_scraping(request):
    top100composers=[]
    page=requests.get('https://digitaldreamdoor.com/pages/best-classic-comp.html')
    soup=BeautifulSoup(page.content, 'html.parser')
    composers_soup = soup.find_all('div',attrs={'class':'list'})
    for i in composers_soup:
        composers = (i.get_text().strip())
        top100composers.append(composers)
        print(composers)
    context = {'top100composers': top100composers}
    return render(request, 'Composers/top100_composers.html', context)