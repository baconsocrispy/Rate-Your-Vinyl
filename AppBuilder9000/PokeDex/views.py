from django.shortcuts import render

# Create your views here.

def pokeDexHome(request):
    return render(request, 'PokeDex/PokeDex_home.html')