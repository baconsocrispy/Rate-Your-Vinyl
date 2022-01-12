from django.shortcuts import render, redirect
from .forms import PokemonForm
from .models import Pokemon


# Create your views here.

def pokeDexHome(request):
    return render(request, 'PokeDex/PokeDex_home.html')
# here we are making it so that we are getting the info from the PokemonForm and saving the info to the database
# if the request.method == post and the form info is valid and then redirecting to the home page for now
def addPokemon(request):
    form = PokemonForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('PokeDex_home')
    content = { 'form': form }
    return render(request, 'PokeDex/AddPokemon_form.html', content)

def show_pokemon(request):
    show_pokemon = Pokemon.object.all()

    context = {'show_pokemon': show_pokemon}
    return render(request, "PokeDex/PokeDex_showPokemon.html", context)