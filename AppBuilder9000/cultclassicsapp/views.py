from django.shortcuts import render, get_object_or_404, redirect
from .forms import CultClassicsForm
from .models import CultClassics


# Creating views
def cultclassicsHome(request):
    return render(request, 'CultClassicsHome.html')

def CultClassicsCreate(request):
    form = CultClassicsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('CultClassicsCreate')
    else:
        print(form.errors)
        form = CultClassicsForm()
    context = {'form': form}
    return render(request, 'CultClassicsCreate.html', context)

def CultClassicsMovies(request):
    cultclassics = CultClassics.objects.all()
    return render(request, 'CultClassicsMovies.html', {'cultclassics': cultclassics})
