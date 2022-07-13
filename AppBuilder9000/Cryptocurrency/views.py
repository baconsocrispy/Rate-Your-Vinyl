from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review


# Create your views here.

#Story #1
def Cryptocurrency_home(request):
    return render(request, "Cryptocurrency/Cryptocurrency_home.html")

#Story 2 function to render built in form from my model Review

def cryptocurrency_addreview(request):
    form = ReviewForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('..')
    content = {'form': form}
    return render(request, 'Cryptocurrency/Cryptocurrency_AddReview.html', content)

#Story 3 Add in a function that gets all the items from the database and sends them to the template

def cryptocurrency_reviews(request):
    cryptocurrecy_reviews = Review.objects.all()
    content = {'cryptocurrency_reviews': cryptocurrecy_reviews}
    return render(request, 'Cryptocurrency/Cryptocurrency_Reviews.html', content)