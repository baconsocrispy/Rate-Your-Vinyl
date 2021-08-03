from django.shortcuts import render, redirect, get_object_or_404
from .forms import NeighborhoodForm, ReviewForm
from .models import Neighborhood, Review
from django.db.models import Count, F, Value, Avg
import requests
from bs4 import BeautifulSoup



#takes you to homepage.


def neighborhoodReview_home(request):
    form = ReviewForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['neighborhood_id']
        return reviewpage(request, pk)
    content = {'form': form}
    return render(request, "NeighborhoodReview/NeighborhoodReview_home.html", content)


# creates a neighborhood to be reviewed.


def create_neighborhood(request):
    form = NeighborhoodForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('NeighborhoodReview/NeighborhoodReview_home.html')
    content = {'form': form}
    return render(request, 'NeighborhoodReview/CreateNewNeighborhood.html', content)

# allows you to filter neighborhood and see reviews.


def reviewpage(request, pk):
    neighborhood = get_object_or_404(Neighborhood, pk=pk)
    reviews = Review.Reviews.filter(neighborhood_id=pk)
    form = ReviewForm(data=request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()
    content = {'neighborhood_id': neighborhood, 'reviews': reviews}
    return render(request, 'NeighborhoodReview/ReviewPage.html', content)

#this is take you to the page where you can write a review. After review is written you will directed to the
#main to see all reviews for the neighborhood


def review(request):
    form = ReviewForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
           # pk = request.POST['id']
           # form.save()
            return redirect('NeighborhoodReview/NeighborhoodReview_home.html')
    content = {'form': form}
    return render(request, 'NeighborhoodReview/CreateReview.html', content)

#This method allow creates a query object that returns everything from the Neighborhood module/table


def details(request):
    neigh_list = Neighborhood.objects.all()
    detail_content = {'neigh_list': neigh_list}
    return render(request, 'NeighborhoodReview/DisplayAllNeighborhoods.html', detail_content)


#this method creates a filters out detail on a specific neighborhood based on pk
#it returns all the fields in the neighborhood field as well as the average rating
#for the neighborhood.


def item_details(request, id):

    neigh_item = get_object_or_404(Neighborhood, id=id)
    reviews = Review.Reviews.filter(neighborhood_id=id)
    avg_rating = reviews.aggregate(Avg('rating'))  # creates a dictionary with name rating__avg
    item_content = {'neigh_item': neigh_item, 'avg_rating': avg_rating}
    return render(request, 'NeighborhoodReview/DisplayNeighborhood_item.html', item_content)


def edit_neighborhood(request, pk):
    item = get_object_or_404(Neighborhood, pk=pk)
    form = NeighborhoodForm(data=request.POST or None, instance=item)  # selects an instance of a neighborhood
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../neighborhood_item_details')
    content = {'form': form}
    return render(request, 'NeighborhoodReview/edit.html', content)


# deletes neighborhood, then sends you to confirmation page where neighborhood can be perminately deleted.


def delete_neighborhood(request, pk):
    pk = int(pk)
    item = get_object_or_404(Neighborhood, pk=pk)
    form = NeighborhoodForm(data=request.POST or None, instance=item)  # selects an instance of a neighborhood
    if request.method == 'POST':
        item.delete()
        return redirect('NeighborhoodReview/DisplayAllNeighborhoods.html')
    content = {"item": item, "form": form}
    return render(request, 'NeighborhoodReview/DeleteNeighborhood.html', content)


def edit_review(request, id):
    item = get_object_or_404(Review, id=id)
    form = ReviewForm(data=request.POST or None, instance=item)  # selects an instance of a neighborhood
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../review_item_detail/')
    content = {'form': form}
    return render(request, 'NeighborhoodReview/edit_review.html', content)


def delete_review(request, id):

    item = get_object_or_404(Review, id=id)
    form = ReviewForm(data=request.POST or None, instance=item)  # selects an instance of a neighborhood
    if request.method == 'POST':
        item.delete()
        return redirect('NeighborhoodReview/Review_Details.html')
    content = {"item": item, "form": form}
    return render(request, 'NeighborhoodReview/DeleteReview.html', content)


#renders an html of all reviews, so that user can select and delete ones deemed "inappropriate"


def review_details(request):
    review_list = Review.Reviews.all()
    content = {'review_list': review_list}
    return render(request, 'NeighborhoodReview/Review_Details.html', content)


def review_item(request, id):

    item = Review.Reviews.filter(id=id)
    get_item = get_object_or_404(item, id=id)
    item_content = {'get_item': get_item}
    return render(request, 'NeighborhoodReview/Review_items.html', item_content)


def soup_page(request):
    page = requests.get("https://smartasset.com/taxes/oregon-property-tax-calculator")
    soup = BeautifulSoup(page.content, 'html.parser')  #contect to page using beautiful soup.
    data = []
    tax_table = soup.find("div", attrs={"id": "table-pk-16840"})  # find the table with the data, locate the class needed
    rows = tax_table.findAll("tr")  # find all elements in tr or below
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]  # iterate through columns and strip extra space
        data.append([ele for ele in cols if ele])  # if the there's an element in the column append to the data.

    content = {'data': data}
    return render(request, "NeighborhoodReview/BeautifulSoup.html", content)




