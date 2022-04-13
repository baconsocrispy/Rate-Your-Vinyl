from django.shortcuts import render, redirect, get_object_or_404
from .models import Fighter
from .forms import FighterForm

# calls the MuayThai_home home page when requested
def Muay_Thai_Home(request):
    return render(request, 'MuayThai/MuayThai_home.html')

# call template and accept the form inputs for adding to the db
def MuayThai_fighter_entry(request):
    form = FighterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('MuayThai_display_all')
    else:
        print(form.errors)
        form = FighterForm()
    content = {
        'form': form,
    }
    return render(request, 'MuayThai/MuayThai_fighter_entry.html', content)