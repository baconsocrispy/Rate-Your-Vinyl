
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Account, PersonalizedNutrition
from .forms import AccountForm, NutritionalQuery
# Create your views here.

def nutrition_home(request):
    return render(request, 'Nutrition/Nutrition_home.html')


def create_account(request):
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'Nutrition/Nutrition_createnewaccount.html', content)