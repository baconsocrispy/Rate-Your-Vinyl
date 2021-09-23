from django.shortcuts import render

# Displays the Home page
def Reading_Home(request):
    return render(request, 'Reading/Reading_Home.html')