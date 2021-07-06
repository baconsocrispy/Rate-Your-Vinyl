from django.shortcuts import render, get_object_or_404, HttpResponse
from .forms import speciesForm

def zoo_home(request):
    return render(request, 'zoo_home.html')

def zoo_add(request):
    return render(request, 'zoo_add.html')

def add_species(request):
    form = speciesForm(data=request.Post or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('zoo_add')
    content = {'form': form}
    return render(request, 'ZooAnimals/zoo_add.html', content)

