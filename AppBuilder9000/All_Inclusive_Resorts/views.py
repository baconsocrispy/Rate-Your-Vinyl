from django.shortcuts import render

# Create your views here.
def resorts_home(request):
    return render(request, 'All_Inclusive_Resorts/resorts_home.html')