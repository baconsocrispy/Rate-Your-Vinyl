from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm


# Render Home page
def home(request):
    return render(request, "VideoGameReviews/gamereviews_home.html")


# Render Add page and allows it to modify db
def add_review(request):
    form = ReviewForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gamereviews_addreview')
    context = {'form': form, }
    return render(request, 'VideoGameReviews/gamereviews_addreview.html', context)
