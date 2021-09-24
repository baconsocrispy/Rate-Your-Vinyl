from django.shortcuts import render


# Displays the Home page
def InlineSpeedSkates_Home(request):
    return render(request, 'skates_home.html')
