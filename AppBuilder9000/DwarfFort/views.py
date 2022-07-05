from django.shortcuts import render

# Story 1 - Build Basic App
def dfort_home(request):
    return  render(request, 'DwarfFort/dfort_home.html')
