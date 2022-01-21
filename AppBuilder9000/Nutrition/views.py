
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Account, PersonalizedNutrition
from .forms import AccountForm, NutritionalQuery
import requests
from bs4 import BeautifulSoup
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

def display_account_details(request, pk):
    item = get_object_or_404(Account, pk=pk)

    # above : query dB for all data on that particular account

    return render(request, 'Nutrition/Nutrition_details.html', {'item': item})
    # this else says we will be rendering the Nutrition_details.html page for the user (STEP 1):
    # on this page, user will have a chance to make edits to the item he selected from dropdown


def display_nutrition_details(request, pk):
    nutrition_item = get_object_or_404(PersonalizedNutrition, pk=pk)

    # above : query dB for all data on that particular account

    return render(request, 'Nutrition/Nutrition_details.html', {'nutrition_item': nutrition_item})
    # this else says we will be rendering the Nutrition_details.html page for the user (STEP 1):
    # on this page, user will have a chance to make edits to the item he selected from dropdown

def delete_account(request, pk):

    item = get_object_or_404(Account, pk=pk)
    if request.method == 'POST': #initially this will be called on a GET, not a post
                                #as it will GET the confirmDelete.html page to confirm a POST before posting.
        item.delete()
        return redirect('display_db') #go back to products_page after confirming delete
    context = {"item": item,} #passing the record as a dictionary item into context variable
    return render(request, "Nutrition/Nutrition_confirmdelete.html", context)#takes you to a page to confirm your intention

def delete_nutrition(request, pk):

    item = get_object_or_404(PersonalizedNutrition, pk=pk)
    if request.method == 'POST': #initially this will be called on a GET, not a post
                                #as it will GET the confirmDelete.html page to confirm a POST before posting.
        item.delete()
        return redirect('display_db') #go back to products_page after confirming delete
    context = {"item": item,} #passing the record as a dictionary item into context variable
    return render(request, "Nutrition/Nutrition_confirmdelete.html", context)#takes you to a page to confirm your intention

def edit_account(request, pk):

    item = get_object_or_404(Account, pk=pk)
    # above : query dB for all data on that particular product
    aform = AccountForm(data=request.POST or None, instance=item)
    """the data will be from request object's post method...the instance will be all the info for 
    that item...we're saying take the item info (instance) and put it into the fields of that form 
    and call it form"""
    if request.method == 'POST':
        if aform.is_valid():
            aform2 = aform.save(commit=False)
            aform2.save()
            return redirect('display_db')
        else:
            print(aform.errors)
    #STEP 2: the above if statements will run once the user has made item changes and submitted them (POST)
    else:
        return render(request, 'Nutrition/Nutrition_edit.html', {'aform': aform})
    #this else says we will be rendering the present_product.html page for the user (STEP 1):
    #on this page, user will have a chance to make edits to the item he selected from dropdown
    """as you can see above, the form variable has been passed on to the render so that the 
    form with item fields filled in can be rendered on the user's screen...form variable is 
    passed on to the render and will be rendered within the present_product page"""


def edit_nutrition(request, pk):
    item = get_object_or_404(PersonalizedNutrition, pk=pk)
    # above : query dB for all data on that particular product
    nform = NutritionalQuery(data=request.POST or None, instance=item)
    """the data will be from request object's post method...the instance will be all the info for 
    that item...we're saying take the item info (instance) and put it into the fields of that form 
    and call it form"""
    if request.method == 'POST':
        if nform.is_valid():
            nform2 = nform.save(commit=False)
            nform2.save()
            return redirect('display_db')
        else:
            print(nform.errors)
    # STEP 2: the above if statements will run once the user has made item changes and submitted them (POST)
    else:
        return render(request, 'Nutrition/Nutrition_edit.html', {'nform': nform})
    # this else says we will be rendering the present_product.html page for the user (STEP 1):
    # on this page, user will have a chance to make edits to the item he selected from dropdown
    """as you can see above, the form variable has been passed on to the render so that the 
    form with item fields filled in can be rendered on the user's screen...form variable is 
    passed on to the render and will be rendered within the present_product page"""


#_________________TESTING CODE BELOW - UNFINISHED CODE BELOW - TEST CODE BELOW_______________________________


def scraper(request):
    if request.method == 'POST':
        page = requests.get('https://www.nutraingredients-usa.com/')
        soup = BeautifulSoup(page.content, 'html.parser')
        refined = soup.find_all('div', class_='Teaser-text')
        for i in refined:
            i = i.get_text()
            print(i)
        return render(request, 'Nutrition/Nutrition_home.html')
    else:
        return render(request, 'Nutrition/Nutrition_scrapedcontent.html')



"""The above function scrapes https://www.nutraingredients-usa.com/ ... specifically, it looks at the 
two bottom HTML elements within this path: <article class='teaser'> --> <div class='teaser-text'> --> 
<h3 class='teaser-title'> ... SCRAPING THIS 
<p class='teaser-intro'> ... SCRAPING THIS TOO 

It scrapes headlines and teaster-text and prints it in terminal window when template 'scrape' button is clicked."""