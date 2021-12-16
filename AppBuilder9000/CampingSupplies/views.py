from django.shortcuts import get_object_or_404, render,redirect
from .forms import TentForm
from .models import Tent


def Camping_Supplies_Home(request):
    #this function will take the request object and use it to find and display the Camping_Supplies_Home.html

    return render(request, 'Camping_Supplies_Home.html')

def Camping_Supplies_Create(request):
    form = TentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('Camping_Supplies_Create')
    else:
        print(form.errors)
        form = TentForm
        context = {'form': form}
    return render(request, 'create.html', context)

def SuppliesList(request):
    Tents = Tent.object.all()
    return render(request, 'SuppliesList.html', {'Tents': Tents})

def Tent_Details(request, pk):
    details = get_object_or_404(Tent, pk=pk)
    context = {'details': details}
    return render(request, 'Camping_Supplies_Details.html', context)
