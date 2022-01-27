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


    #
    # pk = Profile.object.get(pk=pk)
    # profile = get_object_or_404(Profile, pk=pk)
    # name = profile.first_name
    # team = profile.favorite_team
    # content = {'name': name, 'team': team}
    # return render(request, 'IceHockey/IceHockey_myprofile.html', content)

