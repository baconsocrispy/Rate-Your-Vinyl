from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Games, Dlc, Wishlist
from .forms import GameForm, DlcForm, WishlistForm


def KeyMaster_home(request):
    return render(request, 'KeyMaster_home.html')

def KeyMasterAddGame(request):
    form = GameForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('KeyMaster_home')
    content = {'form': form}
    return render(request, 'KeyMasterAddGame.html', content)

def KeyMasterAddDLC(request):
    form = DlcForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('KeyMaster_home')
    content = {'form': form}
    return render(request, 'KeyMasterAddDLC.html', content)

def KeyMasterAddWishlist(request):
    form = WishlistForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('KeyMaster_home')
    content = {'form': form}
    return render(request, 'KeyMasterWishlist.html', content)