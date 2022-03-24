from bs4 import BeautifulSoup
from django.shortcuts import render, redirect, get_object_or_404
import requests
from .forms import KnifeForm
from .models import ChefKnives


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


# def chefknives_soup(request):
#     res = requests.get("https://en.wikipedia.org/wiki/Chef%27s_knife")
#     soup = BeautifulSoup(res.text, 'html.parser').select('body')[0]
#     paragraphs = []
#     images = []
#     link = []
#     heading = []
#     remaining_content = []
#
#     for tag in soup.find_all():
#         if tag.name=="p":
#             paragraphs.append(tag.text)
#         elif tag.name=="img":
#             images.append(url+tag['src'])
#         elif tag.name=="a":
#             if "href" in str(tag)
#                 if "https://en.wikipedia.org/wiki/Chef%27s_knife" not in str(tag['href'])
#     print(knives)
#
#     context = {'knives': knives}
#     return render(request, 'ChefKnives/ChefKnives_Soup.html', context)

    # knives = []
    # page = requests.get("https://www.goodhousekeeping.com/cooking-tools/best-kitchen-knives/g646/best-kitchen-cutlery/")
    # soup = BeautifulSoup(page.content, 'html.parser')
    # knives_soup = soup.find('div', class_='listicle-body-content')
    # knife = knives_soup.find('div', class_='slideshow-slide-dek')
    #
    # for i in knife:
    #     knifes = i.text
    #     knives.append(knifes)
    #
    # print(knives)
    #
    # context = {'knives': knives}
    # return render(request, 'ChefKnives/ChefKnives_Soup.html', context)
