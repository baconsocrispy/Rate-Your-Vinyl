from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestaurantForm, DishForm
from .models import Restaurant, Dish
from operator import attrgetter
import argparse
import json
import pprint
import requests
import sys
import urllib
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode


def MyThai_home(request):
    return render(request, 'MyThai/MyThai_home.html')


def new_restaurant(request):
    # Store Restaurant form as form
    form = RestaurantForm(data=request.POST or None)
    if request.method == 'POST':
        # If form is valid save and return to dishes page.
        if form.is_valid():
            form.save()
            return redirect('MyThai_my_restaurants')
        else:
            # If form isn't valid return to the add page with the content entered.
            content = {'form': form}
            return render(request, 'MyThai/MyThai_add_restaurant.html', content)
    content = {'form': form}
    return render(request, 'MyThai/MyThai_add_restaurant.html', content)


def new_dish(request):
    form = DishForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('MyThai_my_restaurants')
        else:
            content = {'form': form}
            return render(request, 'MyThai/MyThai_add_dish.html', content)
    content = {'form': form}
    return render(request, 'MyThai/MyThai_add_dish.html', content)


def my_restaurants_view(request):
    # Store objects from DB in object as dict.
    dish_list = Dish.objects.all()
    # GET search & sort data for table
    get_dish_query = request.GET.get('get_dish')
    my_sort = request.GET.get('dishes')

    if is_valid_query(get_dish_query):  # If 'is valid' = True, filter the queryset
        dish_list = dish_list.filter(
            # Turn filters into objects to pass to filter()
            Q(dishName__icontains=get_dish_query) |  # Search by dish name & restaurant name
            Q(restaurant__name__icontains=get_dish_query)).distinct()  # Returning only distinct entries

    dish_list = my_sorted(dish_list, my_sort)  # Sort qs
    paginator = Paginator(dish_list, 10)  # Create paginator object with 10 restaurants per page
    page = request.GET.get('page')  # Store paginator object with current page
    dishes = paginator.get_page(page)

    context = {'dishes': dishes}
    return render(request, 'MyThai/MyThai_my_dishes.html', context)


def is_valid_query(param):
    return param != '' and param is not None  # Makes sure search is valid query, if not return false


def my_sorted(dish_list, my_sort):
    if my_sort == 'rating':  # If sorted by rating, reverse so highest goes at the top.
        asc = True
    elif my_sort is None:  # If my_sort is None, sort by dish name
        my_sort = 'dishName'
        asc = False
    else:
        asc = False
    dish_list = sorted(dish_list, key=attrgetter(my_sort), reverse=asc)  # Sort dict by model attribute = 'my_sort'
    return dish_list


def details(request, pk):
    pk = int(pk)
    dish = get_object_or_404(Dish, pk=pk)
    context = {'dish': dish}
    return render(request, 'MyThai/MyThai_details.html', context)


def restaurant_details(request, pk):
    pk = int(pk)
    restaurant = get_object_or_404(Restaurant, pk=pk)
    context = {'restaurant': restaurant}
    return render(request, 'MyThai/MyThai_rest_details.html', context)


def dish_edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Dish, pk=pk)
    form = DishForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        save_edit(form)  # If form is valid, save and redirect to all dishes page
        return redirect('MyThai_my_restaurants')
    else:
        return render(request, 'MyThai/MyThai_dish_edit.html', {'form': form})


def restaurant_edit(request, pk):
    pk = int(pk)
    item = get_object_or_404(Restaurant, pk=pk)
    form = RestaurantForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        save_edit(form)
        return redirect('MyThai_my_restaurants')
    else:
        return render(request, 'MyThai/MyThai_rest_edit.html', {'form': form})


def save_edit(form):
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
    else:
        print(form.errors)


def dish_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('MyThai_my_restaurants')
    context = {"item": item}
    return render(request, "MyThai/MyThai_delete.html", context)


def restaurant_delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('MyThai_my_restaurants')
    context = {"item": item}
    return render(request, "MyThai/MyThai_delete.html", context)


def dish_confirmed(request):
    if request.method == 'POST':
        form = DishForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('MyThai_my_restaurants')
        else:
            return redirect('MyThai_my_restaurants')


def restaurant_confirmed(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('MyThai_my_restaurants')
        else:
            return redirect('MyThai_my_restaurants')


def api_page(request):
    DEFAULT_TERM = 'thai'
    DEFAULT_LOCATION = 'Portland, OR'
    input_values = ''
    try:
        query_api(input_values.term, input_values.location)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )
    return render(request, 'MyThai_api.html', {})


def api_request(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = '{}{}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer%s' % api_key,
    }

    print('Querying {} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def get_business(api_key, business_id):
    API_HOST = 'https://api.yelp.com'
    BUSINESS_PATH = '/v3/businesses/'

    business_path = BUSINESS_PATH + business_id

    return api_request(API_HOST, business_path, api_key)


def api_search(api_key, term, location):
    API_HOST = 'https://api.yelp.com'
    SEARCH_PATH = '/v3/businesses/search'
    SEARCH_LIMIT = 10

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return api_request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def query_api(term, location):
    API_KEY = 'QEFNe77PDTdEruX0EeI91uyTUrJg4NG0guiDraZ8pFkyeED1XUTvlv1zTcOgYmoTVxxHCGCMGUVQs5XRwxM4CxOrUTBjECcZTwsMwF3phWshUH_tdRL4hDseyaqBYHYx '

    response = api_search(API_KEY, term, location)
    businesses = response.get('businesses')

    if not businesses:
        print('No businesses for {} in {} found.'.format(term, location))
        return

    business_id = businesses[0]['id']

    print('{} businesses found, querying business info for top result "{}" ...'.format(
        len(businesses), business_id))
    response = get_business(API_KEY, business_id)

    print('Result for business "{}" found:'.format(business_id))
    pprint.pprint(response, indent=2)
