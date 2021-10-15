from django.shortcuts import render, redirect, get_object_or_404
from .models import Music
from .forms import MusicForm


# Create your views here.
def home(request):
      return render(request,'hiki_home.html')



def music(request):
      form = MusicForm(data=request.POST or None)
      if form.is_valid():
            form.save()
            return redirect('hiki_music')
      else:
            print(form.errors)
      context = {'form': form}
      return render(request,'hiki_music.html',context)
