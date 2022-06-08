#importing render and redirect to help render the webpages and redirect when necessary
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
#import the dogs form form the forms.py
from .forms import DogsForm
#import the class dogs from the models.py
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


# Calling the details template
def details_dogs(request, pk):
    pk = int(pk)
    all_Dogs = get_object_or_404(Dogs, pk=pk)
    form = DogsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('../details')
    content = {
        'all_Dogs': all_Dogs,
        'form': form,
    }
    return render(request, "Dogs/Dogs_details.html", content)
