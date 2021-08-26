from django.shortcuts import render


# Displays Home Page
def BlazerStats_Home(request):
    return render(request, 'BlazerStats/home.html')
