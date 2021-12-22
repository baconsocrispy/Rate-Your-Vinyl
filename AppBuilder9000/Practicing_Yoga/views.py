from django.shortcuts import render, HttpResponse

# Adding function to render home page.
def home(request):
    return render(request, 'yoga_home.html')
