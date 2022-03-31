from django.shortcuts import render, redirect, get_object_or_404
from .forms import CartoonForm
from .models import Cartoon
import requests
from bs4 import BeautifulSoup

# Create your views here.
""" HOME, CREATE, DISPLAY SECTION """
def Cartoons(request):
    return render(request, 'Cartoons/Cartoons_home.html')

def CreateCartoon(request):
    form = CartoonForm(data=request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('Cartoons_home')
    context = {'form': form}
    return render(request, "Cartoons/Cartoons_create.html", context)

def DisplayCartoons(request):
    cartoon_list = Cartoon.Cartoons.all().order_by("premier_date")
    context = {'cartoon_list': cartoon_list}
    return render(request, 'Cartoons/Cartoons_list.html', context)

def DisplayDetails(request, pk):
    item = get_object_or_404(Cartoon, pk=pk)
    context = {'item': item}
    return render(request, 'Cartoons/Cartoons_details.html', context)

""" EDIT, DELETE SECTION """
def DeleteItem(request, pk):
    context = {}
    item = get_object_or_404(Cartoon, pk=pk)

    if request.method == "POST":
        item.delete()
        return redirect("Cartoons_list")

    return render(request, "Cartoons/Cartoons_delete.html", context)

def UpdateItem(request, pk):
    item = Cartoon.Cartoons.get(pk=pk)
    form = CartoonForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('Cartoons_list')

    context = {'item': item, 'form': form}
    return render(request, 'Cartoons/Cartoons_up_date.html', context)

""" BEAUTIFULSOUP SECTION """
def RankingScrape(request):
    # set up a blank list
    top_cartoons = []
    # set up BeautifulSoup
    source = requests.get("https://www.indiewire.com/feature/best-animated-series-all-time-cartoons-anime-tv-1202021835/5/")
    bs = BeautifulSoup(source.content, 'html.parser')
    # Get all the h3 tags under the div 'entry-content' from source site
    rankings = bs.find('div', class_='entry-content')
    rank = rankings.find_all('h3')
    # for loop through the h3 tags but in reverse order (because they are displayed reversed on the source page)
    for i in reversed(rank):
        titles = i.text
        top_cartoons.append(titles)
    print(*top_cartoons)
    context = {'top_cartoons': top_cartoons}
    return render(request, 'Cartoons/Cartoons_rankings.html', context)