from django.shortcuts import render

# Displays the Home page
def EdTech_Home(request):
    return render(request, 'EdTech/EdTech_Home.html')
