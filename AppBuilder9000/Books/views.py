from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddBookForm


def books_home(request):
    return render(request, 'Books/Books_Home.html')


def books_addbook(request):
    form = AddBookForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('books_home')
    content = {'form': form}
    return render(request, 'Books/Books_AddBook.html', content)
