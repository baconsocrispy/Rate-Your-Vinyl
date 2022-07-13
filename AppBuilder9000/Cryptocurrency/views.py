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

