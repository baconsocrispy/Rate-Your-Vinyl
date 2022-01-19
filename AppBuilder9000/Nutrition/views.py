
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
            return redirect('Nutrition_home')
    content = {'form': form}
    return render(request, 'Nutrition/Nutrition_createnewaccount.html', content)

def make_query(request):
    form = NutritionalQuery(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Nutrition_home')
    content = {'form': form}
    return render(request, 'Nutrition/Nutrition_makequery.html', content)

def display_db(request):#methods are always lower case as a naming convention
    accounts = Account.Accounts.all()
    nutritionqueries = PersonalizedNutrition.Personalized.all()

    content = {'accounts': accounts, 'nutritionqueries': nutritionqueries}
    return render(request, 'Nutrition/Nutrition_displaydb.html', content)

def display_details(request, pk):
    item = get_object_or_404(Account, pk=pk)
    # above : query dB for all data on that particular account

    return render(request, 'Nutrition/Nutrition_details.html', {'item': item})
    # this else says we will be rendering the Nutrition_details.html page for the user (STEP 1):
    # on this page, user will have a chance to make edits to the item he selected from dropdown
