from django.shortcuts import render



def home(request):
    return render(request, 'DNDCharacters/dnd_characters_home.html')