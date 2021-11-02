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

def KeyMaster_Gamelist(request):
    game_list = Games.objects.all().order_by('game_name')
    wish_list = Wishlist.objects.all().order_by('game_title')
    return render(request, 'KeyMaster_Gamelist.html', {'game_list': game_list, 'wish_list': wish_list})

def details(request, pk):
    games = get_object_or_404(Games, pk=pk)
    content = {'games': games}
    return render(request, 'KeyMasterGameDetail.html', content)

def wish_details(request, pk):
    wish = get_object_or_404(Wishlist, pk=pk)
    content = {'wish': wish}
    return render(request, 'KeyMasterWishDetail.html', content)