from django.shortcuts import render,redirect
from .models import description
from .forms import descriptionForm



def Cars(request):
    return render(request, 'CarsHome.html')


def CarCreate(request):
    form = descriptionForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('Carhome')
    else:
        return render(request, 'CarCreate.html', {'form': form})

def CarsEntries(request):
    CarsEntries() = Cars.all
    return render(request, 'templates/CarsEntries.html', {'Cars': Cars})

def CarsDetails(request, pk):
    CarsDetails() = get_object_or_404(Album, pk=pk)
    content = {'CarsDetails': CarsDetails()}
    return render(request, 'templates/CarsDetails.html', content)
