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
    return render(request,'hiki_entries.html',context)

#details page
def submissions (request,pk):
      entry = get_object_or_404(Music,pk=pk)
      form = MusicForm(data=request.POST or None, instance=entry)
      if request.method =='POST':
            if form.is_valid():
                  form = form.save(commit=False)
                  form.save()
                  return redirect('hiki_music')
            else:
                  print(form.errors)
      else:
            return render(request,'hiki_details.html', {'form': form})


def editer(request, id):
      edits = Music.Songs.all(Music,pk=id)
      form = MusicForm(request.POST or None,instance=edits)
      if form.is_valid():
            form.save()
            return redirect('hiki_music')
      return render(request,'hiki_edit.html', {'edits': edits, 'form':form})




