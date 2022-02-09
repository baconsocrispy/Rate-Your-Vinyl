from django.shortcuts import get_object_or_404, redirect, render

from .forms import Trails_Form
from .models import AtvTrails
import requests
from bs4 import BeautifulSoup


# this will return to the home page
def Atv_home(request):
    return render(request, 'AtvTrails_home.html')


def add_trail(request):
    form = Trails_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('Atv_home')
    else:
        print(form.errors)
        form = Trails_Form
        context = {'form': form}
    return render(request, 'AtvTrails_create.html', context)


def list_trails(request):
    trails = AtvTrails.objects.all()
    return render(request, 'AtvTrails_list.html', {'trails': trails})


def trail_details(request, pk):
    details = get_object_or_404(AtvTrails, pk=pk)
    context = {'details': details}
    return render(request, 'AtvTrails_details.html', context)


def trail_edit(request, pk):
    show_trail = get_object_or_404(AtvTrails, pk=pk)
    form = Trails_Form(data=request.POST or None,
                       instance=show_trail)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('trail_details', pk)
    context = {'form': form}
    return render(request, 'AtvTrails_edit.html', context)


def trail_delete(request, pk):
    show_trail = get_object_or_404(AtvTrails, pk=pk)
    form = Trails_Form(data=request.POST or None, instance=show_trail)
    if request.method == 'POST':
        show_trail.delete()
        return redirect('list_trails')
    return render(request, 'AtvTrails_delete.html', {'show_trail': show_trail, 'form': form})


# Starting Beautiful Soup Section here
def trail_scrape(request):
    page = requests.get("https://www.alltrails.com/?ref=header")
    soup = BeautifulSoup(page.content, 'html.parser')
    trail_soup = soup.find('div', class_="styles-module__container___bxZSF")
    trending_trails = trail_soup.find_all(class_="styles-module__title___kLkaF")
    for i in trending_trails:
        trails = i.text
        print(trails)
    return render(request, 'AtvTrails_bs.html')
