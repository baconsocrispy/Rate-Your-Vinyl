from django.shortcuts import render
from .forms import UserForm

def Nutrition_Home(request):
    return render(request, "Nutrition/Nutrition_Home.html")

def create(request):
    return render(request, "Nutrition/Nutrition_create.html")

def registerform(request):
    form = UserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Nutrition_Home')
    context = {'form':form}
    return render(request, 'Nutrition/Nutrition_create.html', context)