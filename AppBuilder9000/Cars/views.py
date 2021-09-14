from django.shortcuts import render,redirect,get_object_or_404
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
    CarsEntries = description.objects.all()
    content = {'CarsEntries': CarsEntries}
    return render(request, 'CarsEntries.html', content)

def CarsDetails(request, pk):
    CarsDetails = get_object_or_404(description, pk=pk)
    content = {'CarsDetail': CarsDetail}
    return render(request, 'CarsDetails.html', content)
