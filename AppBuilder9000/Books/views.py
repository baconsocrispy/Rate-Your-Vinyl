from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddBookForm
from .models import AddBook
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
from django.contrib import messages


# render home page
def books_home(request):
    return render(request, 'Books/Books_Home.html')


# function to render built in form from my model AddBook
def books_add_book(request):
    form = AddBookForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('books_reviews')
    content = {'form': form}
    return render(request, 'Books/Books_AddBook.html', content)


# function to fetch all objects created from form and render
def books_reviews(request):
    book_entries = AddBook.objects.all()
    content = {'book_entries': book_entries}
    return render(request, 'Books/Books_Reviews.html', content)


# function to get all attributes of object and render on details page
def books_details(request, pk):
    details = get_object_or_404(AddBook, pk=pk)
    context = {'details': details}
    return render(request, 'Books/Books_Details.html', context)


# function to delete AddBook object
def books_delete(request, pk):
    delete_book = AddBook.objects.get(pk=pk)
    if request.method == 'POST':
        delete_book.delete()
        return redirect('books_reviews')
    return render(request, 'Books/Books_Delete.html')


# function to update AddBook form, instance argument fills fields with selected element.
def books_update(request, pk):
    update_books = AddBook.objects.get(pk=pk)
    form = AddBookForm(request.POST or None, instance=update_books)
    if form.is_valid():
        form.save()
        return redirect('books_reviews')
    return render(request, 'Books/Books_Update.html',
                  {'update_books': update_books,
                   'form': form})


def books_api(request):
    url = "https://bookshelves.p.rapidapi.com/books"

    headers = {
        "X-RapidAPI-Host": "bookshelves.p.rapidapi.com",
        "X-RapidAPI-Key": "1aed881129msh0e4e702933d3b57p1d0a71jsnaba2c0d6b2f8"
    }

    response = requests.request("GET", url, headers=headers)

    print(response)
    books_info = json.loads(response.text)
    thebooks = json.dumps(books_info, indent=4)
    print(thebooks)
    context = {
        'thebooks': thebooks
    }
    return render(request, 'Books/Books_API.html', context)
    # I would like the title, imgUrl, review and description keys from this API and to render in a readable format in my template.

