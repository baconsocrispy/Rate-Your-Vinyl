from django.shortcuts import render, redirect, get_object_or_404
from .models import Resource
from .forms import ResourceForm

# Displays the Home page
def EdTech_Home(request):
    resources = Resource.objects.all()
    return render(request, 'EdTech/EdTech_Home.html')

def EdTech_Create(request):
    form = ResourceForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        result = form.save()
        return redirect('Add_EdTech')
    else:
        return render(request, 'EdTech/EdTech_Create.html', {'form': form})

def EdTech_Entries(request):
    entries = Resource.objects.all()
    content = {'entries': entries}
    return render(request, 'EdTech/EdTech_Entries.html', content)


def EdTech_Details(request, pk):
    details = get_object_or_404(Resource, pk=pk)
    context = {'details': details}
    return render(request, "EdTech/EdTech_Details.html", context)




