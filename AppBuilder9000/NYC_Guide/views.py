from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurants
from .forms import RestaurantForm
import requests

def home(request):
    return render(request, 'NYC_Guide/nyc_home.html')

# add a restaurant
def add_rest(request):
    form= RestaurantForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('nyc_guide_home')
    content = {'form': form}
    return render(request, 'NYC_Guide/add_rest.html', content)

# shows all restaurants from database
def all_rest(request):
    every_rest= Restaurants.Restaurants.all()
    context= {'every_rest': every_rest}
    return render(request, 'NYC_Guide/all_rest.html', context)

# shows details of one item
def details(request, restaurants_id):
    rest_request= get_object_or_404(Restaurants, pk=restaurants_id)
    context= {'rest_request': rest_request}
    return render(request, 'NYC_Guide/details.html', context)


# search a restaurant via search bar
def search_rest(request):
    if request.method == "POST":
        searched= request.POST['searched']
        restaurants= Restaurants.Restaurants.filter(restaurant_name__contains=searched)
        context= {'searched': searched, 'restaurants': restaurants}
        return render(request, 'NYC_Guide/search.html', context)
    else:
        return render(request, 'NYC_Guide/search.html', {})

# update a restaurant
def update_rest(request, restaurants_id):
    restaurant = get_object_or_404(Restaurants, pk=restaurants_id)
    form= RestaurantForm(request.POST or None, instance=restaurant)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('all_rest')
    context= {'form': form, 'restaurant': restaurant}
    return render(request, 'NYC_Guide/update.html', context)

# Delete a restaurant
def delete(request, restaurants_id):
    restaurant= get_object_or_404(Restaurants, pk=restaurants_id)
    form= RestaurantForm(request.POST or None, instance=restaurant)
    if request.method== "POST":
        restaurant.delete()
        return redirect('all_rest')
    context= {'form': form, 'restaurant': restaurant}
    return render(request, 'NYC_Guide/delete.html', context)


def opentable(request):
    response=requests.get('https://opentable.herokuapp.com/api')
    print(response.json())
    return render(request, 'NYC_Guide/opentable.html')

# going to attempt to play around with func below so ignore for now
# def opentable2(request):
#     restaurant = []
#     if 'id' in request.GET:
#         id = request.GET['id']
#         url = 'https://opentable.herokuapp.com/api/restaurants/%s' % id
#         response = requests.get(url)
#         restaurant = response.json()
#         print()
#     return render(request, 'NYC_Guide/opentable.html', {'restaurant': restaurant})