from django.shortcuts import render

def books_home(request):
    return render(request, 'Books/Books_Home.html')
