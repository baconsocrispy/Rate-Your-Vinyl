from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddBookForm
from .models import AddBook


# render home page
def books_home(request):
    return render(request, 'Books/Books_Home.html')


# function to render built in form from my model AddBook
def books_add_book(request):
    form = AddBookForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('books_home')
    content = {'form': form}
    return render(request, 'Books/Books_AddBook.html', content)


# function to fetch all objects created from form and render
def books_reviews(request):
    book_entries = AddBook.objects.all()
    content = {'book_entries': book_entries}
    return render(request, 'Books/Books_Reviews.html', content)


def books_details(request, pk):
    details = get_object_or_404(AddBook, pk=pk)
    context = {'details': details}
    return render(request, 'Books/Books_Details.html', context)
