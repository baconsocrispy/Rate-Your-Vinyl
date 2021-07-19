from django.shortcuts import render, redirect, get_object_or_404
from .models import PreciousMetalsItem
from .forms import MetalForm
import http.client
import mimetypes
import requests


# Create your views here.

# home html

def home(request):
    return render(request, 'PreciousMetals_home.html', {})


# add inventory

def inventory(request):
    form = MetalForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('PreciousMetals_inventory')
    content = {'form': form}
    return render(request, 'PreciousMetals_inventory.html', content)


# query all items in inventory

def list_items(request):
    inv_list = PreciousMetalsItem.metals.all()
    return render(request, 'PreciousMetals_listing.html', {'inv_list': inv_list})


# single item details


def item_details(request, id):
    item_dets = get_object_or_404(PreciousMetalsItem, id=id)
    inv_content = {'item_dets': item_dets}
    return render(request, 'PreciousMetals_details.html', inv_content)


# edit an item


def edit_item(request, id):
    item_dets = get_object_or_404(PreciousMetalsItem, id=id)
    form = MetalForm(request.POST or None, instance=item_dets)
    if form.is_valid():
        form.save()
        return redirect('PreciousMetals_listing')
    content = {'form': form}
    return render(request, 'PreciousMetals_edit.html', content)


# delete item


def delete_item(request, id):
    item_dets = get_object_or_404(PreciousMetalsItem, id=id)
    if request.method == 'POST':
        item_dets.delete()
        return redirect('PreciousMetals_listing')
    delete = {'item_dets': item_dets}
    return render(request, 'PreciousMetals_delete.html', delete)


# api for rates on metals

def rates(request):
    conn = http.client.HTTPSConnection("www.goldapi.io")
    payload = ''
    headers = {
        'x-access-token': 'goldapi-6buwskraz9tg4-io',
        'Content-Type': 'application/json',
    }
    response = conn.request(
        "GET", 'https://www.goldapi.io/api/:metal/:currency/', payload, headers)
    metalrates = response.json()
    return render(request, 'PreciousMetals_rates.html', {
        "timestamp": metalrates[1626721039],
        "metal": metalrates["XAU"],
        "currency": metalrates["USD"],
        "exchange": metalrates["FOREXCOM"],
        "symbol": metalrates["FOREXCOM:XAUUSD"],
        "prev_close_price": metalrates[1812.21],
        "open_price": metalrates[1812.21],
        "low_price": metalrates[1795.09],
        "high_price": metalrates[1817.38],
        "price": metalrates[1807.77],
        "ask": metalrates[1808.17],
        "bid": metalrates[1807.42],
    })
