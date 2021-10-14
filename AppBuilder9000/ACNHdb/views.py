from django.shortcuts import render
from .forms import *
from .models import *



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
    Items = Item.Items.all()
    return render(request, 'anch_collection.html',
                  {'Items': Items})

