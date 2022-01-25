
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Account, PersonalizedNutrition
from .forms import AccountForm, NutritionalQuery
import requests
import json
from bs4 import BeautifulSoup
import pprint
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


#_________________BELOW CODE REPRESENTS THE WEB SCRAPER FUNCTIONALITY OF THE APPLICATION_______________________________


def scraper(request):
    if request.method == 'POST':
        page = requests.get('https://www.nutraingredients-usa.com/')
        soup = BeautifulSoup(page.content, 'html.parser')
        nutrition_data = dict()
        refined = soup.find_all('div', class_='Teaser-text')
        nutrition_data['values'] = [pt.get_text() for pt in refined]
        return render(request, 'Nutrition/Nutrition_home.html',{'nutrition_data': nutrition_data})
    else:
        return render(request, 'Nutrition/Nutrition_scrapedcontent.html')



"""The above function scrapes https://www.nutraingredients-usa.com/ ... specifically, it looks at the 
two bottom HTML elements within this path: <article class='teaser'> --> <div class='teaser-text'> --> 

<p class='teaser-intro'> ... SCRAPING THIS TOO 

It scrapes teaster-text and prints it in terminal window when template 'scrape' button is clicked."""


#_________________BELOW CODE REPRESENTS THE API ACCESS FUNCTIONALITY OF THE APPLICATION_______________________________
"""
API Name: nutritionix has a dB of ~600,000 real food items (e.g. BigMac, Cheetos, large apple, etc.)
and their corresponding nutritional information (e.g. calories, saturated fat, vitamin C, etc.)
API Guide: https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#heading=h.73n49tgew66c
"""

def nutritionix_nutrients_api(request):
    #user_query is the name value of the input element where a user enters a query
    # we are saying if a user has entered a query
    if 'user_query' in request.GET:
        api_version = 'v2'
        api_base_url = f'https://trackapi.nutritionix.com/{api_version}'
        endpoint_path = f'/natural/nutrients'
        endpoint = f'{api_base_url}{endpoint_path}'
        query = request.GET['user_query']
        # requests.post accepts 'headers' as an argument.
        # we provide api credentials, as specified in the API documentation, in 'headers'
        headers = {
            'x-app-id': '212b5e6c',
            'x-app-key': 'bcfd3f08c16996662783976a3b37793a',
            # remote-user-id is used for billing purposes, but this isn't relevant so
            # api told us to use '0' as a value to disregard.
            'x-remote-user-id': '0'
        }

        # the API specified that we need to provide 'query' and 'timezone' key/value pairs.
        # this is stored as a dictionary in variable 'data', an argument that requests.post
        # can accept (requests.post can only accept certain arguments per its documentation)
        data = {
            "query": query,

        }

        # api stated this endpoint requires a POST request.
        # the 'endpoint' argument stores the precise URL endpoint
        # the 'headers' argument stores API credentials (keys)
        # the 'data' argument is what stores the actual query itself
        request = requests.post(endpoint, headers=headers, data=data)



        # prints a status code to verify our request was successful
        print(request.status_code)

        # calls our pprint function, imported from pprint, printing JSON neatly in terminal for legibility
        #the purpose is to show ALL the data the API sends us, in contrast to what we end up with through filtering
        pprint.pprint(request.json())

        #the below function filters JSON response data to include only nutritional info
        #all nutritional info in JSON response starts with 'nf_', hence we targeted only KVPs with 'nf_'' in the key
        if request.status_code in range(200, 299):
            data = request.json()
            results = data['foods']
            search_key = 'nf_'
            out = {}
            for i in results:
                if not isinstance(i, dict):
                    continue
                for k, v in i.items():

                    if search_key in k:
                        out[k] = v
            for k, v in out.items():
                print(k, v)
        #go to home page after printing in terminal
        return redirect('Nutrition_home')
    return render(request, 'Nutrition/Nutrition_API.html')
"""
We are accessing nutritionix's API: a database of ~600,000 real food items (e.g. BigMac, Cheetos, large apple, etc.)
and their corresponding nutritional information (e.g. calories, saturated fat, vitamin C, etc.)

!
"""