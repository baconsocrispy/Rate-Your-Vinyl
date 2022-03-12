from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import SuperCarsForm
from .models import SuperCars

# Create your views here.

def SuperCarsHome(request):
    return render(request, 'SuperCars/SuperCarsHome.html')



def CreateRecord(request):
    form = SuperCarsForm(data=request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('SuperCars_Home')
        else:
            print(form.errors)
            form = SuperCarsForm()
    context = {
         'form': form,
        }

    return render(request, 'SuperCars/CreateRecord.html', context)
