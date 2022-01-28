from django.shortcuts import render, redirect, get_object_or_404
from .form import UserForm
from .models import Profile


def IceHockey_home(request):
    return render(request, 'IceHockey/IceHockey_home.html')


def IceHockey_newprofile(request):
    form = UserForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('IceHockey_home')
    context = {'form': form}
    return render(request, 'IceHockey/IceHockey_newprofile.html', context)


def IceHockey_myprofile(request):
    profile_list = Profile.Profile.all()
    return render(request, 'IceHockey/IceHockey_myprofile.html', {'profile_list': profile_list})


def IceHockey_details(request, pk):
    details = get_object_or_404(Profile, pk=pk)
    context = {'details': details}
    return render(request, 'IceHockey/IceHockey_details.html', context)


def IceHockey_edit(request, pk):
    item = get_object_or_404(Profile, pk=pk)
    form = UserForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('IceHockey_myprofile')
    context = {'form': form}
    return render(request, 'IceHockey/IceHockey_edit.html', context)


def IceHockey_delete(request, pk):
    item = get_object_or_404(Profile, pk=pk)
    form = UserForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('IceHockey_myprofile')
    return render(request, 'IceHockey/IceHockey_delete.html', {'item': item, 'form': form})




