from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import PickupForm
from .models import Pickup


# Create your views here.
def basketballHome(request):
    return render(request, 'Basketball/Basketball_home.html')


def basketballPickup(request):
    form = PickupForm(data=request.POST or None)
    posts = Pickup.games.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    content = {'form': form, 'posts': posts}

    return render(request, 'Basketball/Basketball_Pickup.html', content)
