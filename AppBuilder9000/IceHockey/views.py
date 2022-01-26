from django.shortcuts import render, redirect, get_object_or_404
from .models import User, CreateAPlayer
from .form import UserForm, CreateAPlayerForm


def IceHockey_home(request):

    return render(request, 'IceHockey/IceHockey_home.html')


def IceHockey_create(request):
    form = UserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('IceHockey_home')
    content = {'form': form}
    return render(request, 'IceHockey/IceHockey_home.html', content)

