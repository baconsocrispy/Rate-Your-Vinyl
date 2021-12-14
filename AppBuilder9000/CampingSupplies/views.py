from django.shortcuts import get_object_or_404, render,redirect
from .forms import campingsuppliesform

def Camping_Supplies_Home(request):
    #this function will take the request object and use it to find and display the Camping_Supplies_Home.html

    return render(request, 'Camping_Supplies_Home.html')

def Camping_Supplies_Create(request):
    form = campingsuppliesform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('Camping_Supplies_Create')
    else:
        print(form.errors)
        form = campingsuppliesform
        context = {'form': form}
    return render(request, 'create.html', context)