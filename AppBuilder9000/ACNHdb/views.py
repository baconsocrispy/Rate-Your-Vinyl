from django.shortcuts import render
from .forms import *

def acnh_home(request):
    return render(request, 'acnh_home.html')


def acnh_create(request):
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()

    content = {'form': form}
    return render(request, 'acnh_create.html', content)






def acnh_collection(request):
    data = Item.objects.all()

    itm = {
        "Item": data
    }

    return render("acnh_collection.html", itm)