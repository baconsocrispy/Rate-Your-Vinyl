from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DogsForm


# calls the Dogs_home home page when requested
def Dogs_home(request):
    return render(request, 'Dogs/Dogs_home.html')


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