from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import NovelForm


def home(request):
    return render(request, "Novels/Novels_home.html")


def novelEntry(request):
    form = NovelForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('Novels_create')
    context = {'form': form, }
    return render(request, 'Novels/Novels_create.html', context)


def novelDisplay(request):
    all_novels = Book.objects.all()
    return render(request, 'Novels/Novels_display.html', {'all_novels': all_novels})


def novelDetails(request, pk):
    pk = int(pk)
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'Novels/Novels_details.html', {'book': book})