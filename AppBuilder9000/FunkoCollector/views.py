from django.shortcuts import render

# function linking the html file to the url.py
def funkocollectorhome(request):
    return render(request, 'funkocollectorhome.html')