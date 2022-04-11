from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .forms import TrailReviewForm
from .models import ReviewTrail


def mtb_trails_home(request):
    return render(request, "MTB_Trails/mtb_trails_home.html")


# User data from form to be saved and then user redirected to submitted_review
def mtb_trails_review(request):
    # If this is a POST request we need to process the form data
    form = TrailReviewForm(data=request.POST or None)
    if request.method == 'POST':
        # Check if data is valid:
        if form.is_valid():
            form.save()
            # Process data in form.cleaned_data as required
            # Redirect to new URL
            return redirect("submitted_review")
    else:
        form = TrailReviewForm()
    context = {'form': form}
    return render(request, "MTB_Trails/mtb_trails_review.html", context)


# Simple rendering for success review submission
def submitted_review(request):
    return render(request, "MTB_Trails/submitted_review.html")


# View for user-submitted reviews
def existing_reviews(request):
    trails = ReviewTrail.objects.all()
    return render(request, "MTB_Trails/existing_reviews.html", {'trails': trails})


# View for detailed review page
def review_details(request, pk):
    trail = ReviewTrail.objects.get(pk=pk)
    return render(request, "MTB_Trails/review_details.html", {'trail':trail})


# View for updating or deleting review.
def edit_or_delete(request, pk):
    trail = get_object_or_404(ReviewTrail, pk=pk)
    form = TrailReviewForm(instance=trail)
    if request.method == 'POST':
        form = TrailReviewForm(request.POST, instance=trail)
        # Check if data is valid:
        if form.is_valid():
            form.save()
            # Process data in form.cleaned_data as required
            # Redirect to new URL
            return redirect("submitted_review")
        # Cindy, I don't know why, but changing dictionary to 'trail' won't load form in webpage.
    context = {'form': form,
               'trail': trail}
    return render(request, "MTB_Trails/edit_or_delete.html", context)


# View for delete.
def delete_trail(request, pk):
    trail = get_object_or_404(ReviewTrail, pk=pk)
    context = {'trail': trail}

    trail.delete()

    return redirect('existing_reviews')



















