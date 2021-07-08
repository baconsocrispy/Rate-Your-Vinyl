from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Account
from .forms import AccountForm


def VillagerRegistry_Index(request):
    return render(request, 'Villager_Registry/villager_home.html')


def VillagerList(request):
    return render(request, 'Villager_Registry/villager_list.html')


def VillagerEvents(request):
    return render(request, 'Villager_Registry/villager_events.html')


def VillagerAccount(request):
    return render(request, 'Villager_Registry/villager_account.html')


def create_account(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('villager_account')
    else:
        print(form.errors)
        form = AccountForm()
    context = {
        'form': form,
    }
    return render(request, 'Villager_Registry/villager_CreateNewAccount.html', context)
