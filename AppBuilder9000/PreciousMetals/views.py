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

def listItems(request):
    inven_list = PreciousMetalsItem.metals.all()
    return render(request, 'PreciousMetals_listing.html', {'inven_list': inven_list})

def itemDetails(request, id):
    itemdets = get_object_or_404(PreciousMetalsItem, id=id)
    icontent = {'itemdets': itemdets}
    return render(request, 'PreciousMetals_details.html', icontent)

