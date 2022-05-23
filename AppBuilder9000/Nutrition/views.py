from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from .models import User

def Nutrition_Home(request):
    return render(request, "Nutrition/Nutrition_Home.html")

def create(request):
    return render(request, "Nutrition/Nutrition_create.html")

def registerform(request):
    form = UserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            User = form.save(commit=False)
            User.BMI = (User.Weight * 703) / (User.Height ** 2)
            if User.Gender == 'Male':
                User.FatPercent = (User.BMI * 1.39) + (User.Age * 0.16) - 19.34
            else:
                User.FatPercent = (User.BMI * 1.39) + (User.Age * 0.16) - 9
            if User.BMI >= 25:
                User.Phase = 'Fat Burning'
            elif User.BMI < 25 and User.FatPercent > 15 and User.Gender == 'Male':
                User.Phase = 'Shredding'
            elif User.BMI < 25 and User.FatPercent > 20 and User.Gender == 'Female':
                User.Phase = 'Shredding'
            elif User.BMI < 25 and User.FatPercent <= 15 and User.Gender == 'Male':
                User.Phase = 'Bulking'
            elif User.BMI < 25 and User.FatPercent <= 20 and User.Gender == 'Female':
                User.Phase = 'Bulking'
            if User.Phase == 'Fat Burning' and User.Weight >= 220:
                User.Calories = 2400
                User.Protein = 180
            elif User.Phase == 'Fat Burning' and User.Weight < 220 and User.Weight >= 200:
                User.Calories = 2200
                User.Protein = 165
            elif User.Phase == 'Fat Burning' and User.Weight < 200 and User.Weight >= 180:
                User.Calories = 2000
                User.Protein = 150
            elif User.Phase == 'Fat Burning' and User.Weight < 180 and User.Weight >= 160:
                User.Calories = 1800
                User.Protein = 135
            elif User.Phase == 'Fat Burning' and User.Weight < 160:
                User.Calories = 1600
                User.Protein = 120
            elif User.Phase == 'Shredding':
                User.Calories = User.Weight * 12
                User.Protein = User.Weight * 0.8
            elif User.Phase == 'Bulking':
                User.Calories = User.Weight * 15
                User.Protein = User.Weight
            form.save()
            return redirect('Nutrition_Home')
    context = {'form':form}
    return render(request, 'Nutrition/Nutrition_create.html', context)

def userdetails(request, pk):
    details = get_object_or_404(User, pk=pk)
    context = {'details': details}
    return render(request, 'Nutrition/Nutrition_details.html', context)

def displayusers(request):
    display = User.Users.all()
    context = {'display': display}
    return render(request, 'Nutrition/Nutrition_display.html', context)

def edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(User, pk=pk)
    form = UserForm(data = request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('Nutrition_display')
        else:
            print(form.errors)
    else:
        return render(request, 'Nutrition/Nutrition_edit.html', {'form':form, 'item':item})

def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('Nutrition_display')
    content = {"item":item}
    return render(request, "Nutrition/Nutrition_delete.html", content)

def confirmDelete(request):
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('Nutrition_display')
    else:
        return redirect('Nutrition_display')
