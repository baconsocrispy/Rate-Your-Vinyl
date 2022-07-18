from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
import requests
import json





# Create your views here.

#Story #1
def Cryptocurrency_home(request):
    return render(request, "Cryptocurrency/Cryptocurrency_home.html")

#Story 2 function to render built in form from my model Review

def cryptocurrency_addreview(request):
    form = ReviewForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('..')
    content = {'form': form}
    return render(request, 'Cryptocurrency/Cryptocurrency_AddReview.html', content)

#Story 3 Add in a function that gets all the items from the database and sends them to the template

def cryptocurrency_reviews(request):
    cryptocurrency_reviews = Review.objects.all()
    content = {'cryptocurrency_reviews': cryptocurrency_reviews}
    return render(request, 'Cryptocurrency/Cryptocurrency_Reviews.html', content)

#Story 4 Add in function for cryptocurrency details

def cryptocurrency_details(request, pk):
    details = get_object_or_404(Review, pk=pk)
    content = {'details': details}
    return render(request, 'Cryptocurrency/Cryptocurrency_Details.html', content)

#Story 5 Edit Function

def cryptocurrency_edit(request, pk):
    details = get_object_or_404(Review, pk=pk)
    form = ReviewForm(data=request.POST or None, instance=details)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Cryptocurrency_Reviews')
    content = {'form': form, 'details': details}
    return render(request, 'Cryptocurrency/Cryptocurrency_Edit.html', content)

#Story 5 Delete Function

def cryptocurrency_delete(request, pk):
    details = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        details.delete()
        return redirect('Cryptocurrency_Reviews')
    content = {'details': details}
    return render(request, 'Cryptocurrency/Cryptocurrency_delete.html', content)

#Story 6 API

def cryptocurrency_api(request):
    url = "https://binance46.p.rapidapi.com/ticker/price"

    querystring = {"symbol": "BTCUSDT"}

    headers = {
        "X-RapidAPI-Host": "binance46.p.rapidapi.com",
        "X-RapidAPI-Key": "9475a3c2femshf5feacffd670ac7p141cc0jsn51ca5a864d7c"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    api_pull = json.loads(response.text)
    price = api_pull["price"]  #The element we will pull is the  price of Bitcoin(in USD)
    content = {"price": price}
    return render(request, 'Cryptocurrency/Cryptocurrency_API.html', content)

