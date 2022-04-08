from django.shortcuts import render, get_object_or_404, redirect
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
