from django.shortcuts import render

# Create your views here.
def magic_home(request):
    return render(request, 'Magic/magic_home.html')