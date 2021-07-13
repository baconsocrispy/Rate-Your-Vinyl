from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from .forms import AccountForm


def VillagerRegistry_Index(request):
    return render(request, 'Villager_Registry/villager_home.html')


def PlayerTable(request):
    user_info = Account.info.all()
    entry1 = Account.info.get(pk=1)
    return render(request, 'Villager_Registry/villager_home.html', {"shay": entry1}, user_info)


def VillagerList(request):
    return render(request, 'Villager_Registry/villager_list.html')


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


def Retrieve_PlayerList(request):
    playerset = Account.info.all()
    return render(request, 'Villager_Registry/villager_playerList.html', {'playerset': playerset})


def Retrieve_PlayerDetails(request, pk):
    try:
        playerinfo = Account.info.get(pk=pk)
    except Account.DoesNotExist:
        raise get_object_or_404('Player does not exist')
    return render(request, 'Villager_Registry/villager_playerDetails.html', {'playerinfo': playerinfo})


def ShayDetails(request, pk):
    pk = int(pk)
    playerone = Account.info.get(pk=1)
    return render(request, 'Villager_Registry/villager_home.html', {'playerone': playerone}, pk)


def UpdateDetails(request, pk):
    pk = int(pk)
    try:
        old_info = get_object_or_404(Account, pk=pk)
    except Exception:
        raise get_object_or_404('Does Not Exist')

    if request.method == 'POST':
        form = AccountForm(data=request.POST, instance=old_info)
        if form.is_valid():
            form.save()
            return redirect(f'{pk}/villager_playerDetails')
        else:

            form = AccountForm(instance=old_info)
            context = {
                'form': form
            }
            return render(request, 'Villager_Registry/villager_playerList.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('villager_details')
    context = {"item": item, }
    return render(request, "Villager_Registry/resident_confirmDelete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = AccountForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('villager_details')
    else:
        return redirect('villager_details')

