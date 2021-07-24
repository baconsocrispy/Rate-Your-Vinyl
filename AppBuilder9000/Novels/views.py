from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import NovelForm
from django.contrib import messages

# the basic view when visiting the page
def home(request):
    return render(request, "Novels/Novels_home.html")


# allows new record to be created and saved to dB
def novelEntry(request):
    form = NovelForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Novels_create')
    context = {'form': form, }
    return render(request, 'Novels/Novels_create.html', context)


# displays all records
def novelDisplay(request):
    all_novels = Book.objects.all()
    return render(request, 'Novels/Novels_display.html', {'all_novels': all_novels})


# function allows all data for one record to be viewed and edited
def novelDetails(request, pk):
    pk = int(pk)
    book = get_object_or_404(Book, pk=pk)
    form = NovelForm(data=request.POST or None, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            # want to add an alert that says changes were made. This does not currently work?
            messages.info(request, 'Changes made successfully.')
            return redirect('Novels_display')
        else:
            print(form.errors)
    else:
        return render(request, 'Novels/Novels_details.html', {'form': form})


def novelDelete(request, pk):
    pk = int(pk)
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('Novels_display')
    context = {'book': book}
    return render(request, 'Novels/Novels_delete.html', context)