from django.shortcuts import render

# Create your views here.
def JobScraping_home(request):
    return render(request, 'jobScraping/JobScraping_home.html')