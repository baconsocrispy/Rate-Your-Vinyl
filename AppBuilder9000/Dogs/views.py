from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DogsForm
from .models import Dogs


# calls the Dogs_home home page when requested
def Dogs_home(request):
    return render(request, 'Dogs/Dogs_home.html')

# calls the Dogs Create page, here they will have a form to fill out
# to add to the database
def Dogs_create(request):
    form = DogsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Dogs_home')
    else:
        print(form.errors)
        form = DogsForm()
    content = {'form': form}
    return render(request, 'Dogs/Dogs_create.html', content)

# Displaly the dog's in the Database
def display_dogs(request):
    all_Dogs = Dogs.Dog.all()
    content = {
        'all_Dogs': all_Dogs,
    }
    return render(request, 'Dogs/Dogs_lists.html', content)

