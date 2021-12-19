from django.shortcuts import render, get_object_or_404, redirect
from .forms import CharacterForm
from .models import Characters


def dnd_characters_home(request):
    return render(request, 'DNDCharacters/dnd_characters_home.html')

def admin_console(request):
    characters = Characters.objects.all()
    return render(request, 'DNDCharacters/dnd_character_lookup.html', {'characters': characters})

def dnd_characters_howto(request):
    return render(request, 'DNDCharacters/dnd_characters_HowTo.html')

def createCharacter(request):
    form = CharacterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        form = CharacterForm()
    context = {
        'form': form,
    }
    return render(request, 'DNDCharacters/dnd_characters_Creation.html', context)

def dnd_characters_classdescript(request):
    return render(request, 'DNDCharacters/dnd_characters_ClassDescript.html')

