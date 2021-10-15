from django.shortcuts import render, redirect, get_object_or_404
from .models import Music




# Create your views here.
def home(request):
      return render(request,'hiki_home.html')



def music(request):
      songs = Music.objects.all
      return render(request,'songs/hiki_music.html', {'songs':songs})
