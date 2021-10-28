from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import TheForce
from .forms import TheForceForm
from django.views.generic import FormView

# Create your views here.
def The_Force_home(request):
    return render(request, 'The_Force_Home.html')

def The_Force_Create(request):
        form = TheForceForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('TheForce')

        else:
            print(form.errors)
            form = TheForceForm()
        context = {
            'form': form,
        }
        return render(request, 'The_Force_Create.html', context)



def The_Force_Events(request):
    Event = TheForce.objects.all()
    return render(request, 'TheForce', {'Event': Event})

def The_Force_Costumes(request, pk):
    costumes = get_object_or_404('', pk=pk)
    context = {'costumes': costumes}
    return render(request, TheForce, context)

def Edit(request, pk):
    item = get_object_or_404(TheForce, pk=pk)
    form = TheForceForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('The_Force_Event')

        else:
            print(form.errors)
    else:
        return render(request, The_Force_Create, {'form': form, 'item': item})

def update(request, pk):
     TheForce = The_Force_Costumes().objects.get(pk=pk)
     TheForce.name = request.POST.get('name')
     TheForce.save()
     return redirect('The_Force_Event')

def ConfirmDelete(request, pk):
    item = get_object_or_404('TheForce', pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('The_Force_Event')
    context = {'item': item}
    return render(request, 'The_Force_ConfirmDelete.html', context)







