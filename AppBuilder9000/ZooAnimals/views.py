from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .forms import speciesForm
from .models import Species

def zoo_home(request):
    return render(request, 'zoo_home.html')

def zoo_add(request):
    form = speciesForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('zoo_add')
    else:
        form = speciesForm()
    content = {'form': form}
    return render(request, 'zoo_add.html', content)

def zoo_current(request):
    spec1 = Species.objects.all().order_by('commonName')
    return render(request, 'zoo_current.html', {'spec1': spec1})

def zoo_details(request, id):
    spec_details = get_object_or_404(Species, id=id)
    return render(request, "zoo_details.html", {
        'Common_Name': spec_details.commonName,
        'Latin_Name': spec_details.latinName,
        'Location': spec_details.location,
        'SSP': spec_details.SSP,
    })