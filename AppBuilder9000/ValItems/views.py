from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


def Val_home(request):
    return render(request, 'ValItems/Val_home.html')


def AddItem(request):
    form = ItemForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('AddItem')
    content = {'form': form}
    return render(request, 'ValItems/AddItem.html', content)


def Items(request):
    items = Item.item_object.all()
    return render(request, 'ValItems/Items.html', {'items': items})


def Details(request, pk):
    items = get_object_or_404(Item, pk=pk)
    return render(request, 'ValItems/Details.html', {'items': items})
