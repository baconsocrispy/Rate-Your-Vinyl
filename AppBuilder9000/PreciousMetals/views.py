from django.shortcuts import render, redirect, get_object_or_404
from .models import PreciousMetalsItem
from .forms import MetalForm


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

