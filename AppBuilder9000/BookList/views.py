from django.shortcuts import render, redirect,  get_object_or_404
from .forms import EntryForm
from .models import BookEntry


# Story #1: Build the basic app ----------------------------------------------------------------------------------------

def BookList_Home(request):
    return render(request, 'BookList/BookList_Home.html')


# Story #2: Create your model ------------------------------------------------------------------------------------------

def Book_Entry(request):
    form = EntryForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('BookList_Home')
    content = {'form': form}
    return render(request, 'BookList/BookList_Create.html', content)


# Story #3: Display all items from database ----------------------------------------------------------------------------

def BookList_Display(request):
    entry = BookEntry.BookEntrys.all()
    content = {'entry': entry}
    return render(request, 'BookList/BookList_Display.html', content)

# Story #4: Details page -----------------------------------------------------------------------------------------------

def BookList_Details(request):
    entry = BookEntry.BookEntrys.all()
    content = {'entry': entry}
    return render(request, 'BookList/BookList_Details.html', content)

