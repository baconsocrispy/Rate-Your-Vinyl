from django.shortcuts import render, redirect,  get_object_or_404




# Story #1: Build the basic app ----------------------------------------------------------------------------------------

def BookList_Home(request):
    return render(request, 'BookList/BookList_Home.html')