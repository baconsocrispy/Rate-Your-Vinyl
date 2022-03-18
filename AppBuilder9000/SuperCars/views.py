from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .forms import SuperCarsForm
from .models import SuperCars



def SuperCarsHome(request):
    products = SuperCars.objects.all()
    return render(request, 'SuperCars/SuperCarsHome.html',{'products': products})



def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(SuperCars, pk=pk)
    form = SuperCarsForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('SuperCars_Home')
        else:
            print(form.errors)
    else:
        return render(request, 'SuperCars/PresentRecord.html', {'form': form})
#adding comment

def CreateRecord(request):
    form = SuperCarsForm(data=request.POST or None)
    if request.method =='POST':
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
