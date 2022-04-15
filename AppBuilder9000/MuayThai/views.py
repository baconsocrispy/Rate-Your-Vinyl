from django.shortcuts import render, get_object_or_404, redirect
from .forms import FighterForm
from .models import Fighter

# calls the MuayThai_home home page when requested
def Muay_Thai_Home(request):
    return render(request, 'MuayThai/MuayThai_home.html')

# calls template and accept the form inputs for adding to the db (the create part of it)
def MuayThai_fighter_entry(request):
    form = FighterForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MuayThai_home')

    context = {'form': form}
    return render(request, 'MuayThai/MuayThai_fighter_entry.html', context)


# Display fighter's names
def DisplayFighters(request):
    fighters = Fighter.Fighter.all()
    context = {'fighters': fighters}
    return render(request, 'MuayThai/MuayThai_fighters.html', context)