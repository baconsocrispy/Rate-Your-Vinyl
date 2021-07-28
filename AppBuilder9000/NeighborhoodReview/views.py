from django.shortcuts import render, redirect


def NeighborhoodReview_home(request):
    return render(request, "NeighborhoodReview/NeighborhoodReview_home.html")