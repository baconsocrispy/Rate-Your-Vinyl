from django.shortcuts import render, get_object_or_404, redirect
from .forms import FighterForm
from .models import Fighter

# calls the MuayThai_home home page when requested
def Muay_Thai_Home(request):
    return render(request, 'MuayThai/MuayThai_home.html')

# calls template and accept the form inputs for adding to the db (the create part of it)
def MuayThai_fighter_entry(request):
    form = FighterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MuayThai_display_fighters')
    else:
        print(form.errors)
        form = FighterForm()
    content = {
        'form': form,
    }
    return render(request, 'MuayThai/MuayThai_fighter_entry.html', content)


# Display fighter's names
def MuayThai_display_fighters(request):
    fighters = Fighter.Fighter.all()
    content = {
        'fighters': fighters,
    }
    return render(request, 'MuayThai/MuayThai_display_fighters.html', content)


# call the details template
def MuayThai_fighters_details(request, pk):
    pk = int(pk)
    fighter = get_object_or_404(Fighter, pk=pk)
    form = FighterForm(data=request.POST or None, instance=fighter)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('MuayThai_display_fighters')
        else:
            print(form.errors)

    else:
        content = {
            'form': form,
            'fighter': fighter,
        }
        return render(request, 'MuayThai/MuayThai_fighters_details.html', content)


# call template to confirm we are deleting from the database
def MuayThai_delete_fighter(request, pk, fighter=None):
    pk = int(pk)
    fighter = get_object_or_404(Fighter, pk=pk)
    if request.method == 'POST':
        fighter.delete()
        return redirect('MuayThai_display_fighters')
    content = {
        "fighter": fighter,
    }
    return render(request, "MuayThai/MuayThai_delete.html", content)


# function used to confirm the delete action
def MuayThai_delete(request):
    if request.method == 'POST':
        form = FighterForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('MuayThai_display_fighters')
    else:
        return redirect('MuayThai_display_fighters')

