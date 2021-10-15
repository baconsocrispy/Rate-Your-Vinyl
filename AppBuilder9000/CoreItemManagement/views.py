from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Item, Vendor
from .forms import ItemForm, VendorForm

# Create your views here.
def cim_home(request):
    return render(request, 'cim_home.html')


def cim_new(request):
    form = ItemForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cim_home')
    content = {'form': form}
    return render(request, 'cim_new.html', content)


def cim_newVendor(request):
    form = VendorForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cim_home')
    content = {'form': form}
    return render(request, 'cim_newVendor.html', content)



def cim_edit(request):
    form = Item(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['id']
            form.save()
            return cim_item(request, pk)
    return render(request, 'cim_edit.html')



def cim_editVendor(request):
    form = Vendor(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['id']
            form.save()
            return cim_item(request, pk)
    return render(request, 'cim_editVendor.html')


def cim_list(request):
    _items = get_object_or_404(Item)
    try:
        items = Item.objects.all()

    except Item.DoesNotExist:
        raise Http404("No items found")

    for item in items:
        print(item)

    content = {'items': _items}
    return render(request, 'cim_list.html', content)


def cim_item(request, pk):
    _item = get_object_or_404(Item, pk=pk)

    item = Item


    content = {
        'part_num': item.item_pn,
        'name': item.item_name,
        'count': item.item_count,
        'price': item.item_price,
        'category': item.item_category,
        'vendor': item.item_vendor,
    }
    return render(request, 'cim_item.html', content)

