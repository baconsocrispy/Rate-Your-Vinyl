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


def entries(request):
    items = Music.Songs.all()
    context = {'items':items}
    return render(request,'hiki_entries',context)

#details page
def submissions (request,pk):
      pk = int(pk)
      entry = get_object_or_404(Music,pk=pk)
      form = MusicForm(data=request.Post or None, instance=entry)
      if request.method =='POST':
            if form.is_valid():
                  form2 = form.save(commit=False)
                  form2.save()
                  return redirect('music')
            else:
                  print(form.errors)
      else:
            return render(request,'hiki_details')



