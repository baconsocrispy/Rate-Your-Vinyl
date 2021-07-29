from django.shortcuts import render, redirect, get_object_or_404
from .forms import NeighborhoodForm, ReviewForm
from .models import Neighborhood, Review

#takes you to homepage.


def neighborhoodReview_home(request):
    form = ReviewForm(data=request.POST or None)
    if request.method =='POST':
        pk = request.POST['neighborhood_id']
        return reviewpage(request, pk)
    content = {'form': form}
    return render(request, "NeighborhoodReview/NeighborhoodReview_home.html",content)


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
    content = {'neighborhood_id': neighborhood, 'reviews': reviews}
    return render(request, 'NeighborhoodReview/ReviewPage.html', content)

#this is take you to the page where you can write a review. After review is written you will directed to the
#main to see all reviews for the neighborhood


def review(request):
    form = ReviewForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            pk = request.POST['neighborhood_id']
            form.save()
            return redirect('NeighborhoodReview/NeighborhoodReview_home.html')
    content = {'form': form}
    return render(request, 'NeighborhoodReview/CreateReview.html', content)




