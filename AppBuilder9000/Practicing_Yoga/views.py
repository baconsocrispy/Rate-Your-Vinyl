from django.shortcuts import render, HttpResponse

# Adding function to render home page.
def home(request):
    return render(request, 'Practicing_Yoga/yoga_home.html')
