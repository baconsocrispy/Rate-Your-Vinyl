from django.shortcuts import render, redirect, get_object_or_404
from .forms import accountForm, childForm
from .models import account, singupChild


# Create your views here.
def coachHome(request):
    return render(request, 'Jobs/coachHome.html')

def coachCreate(request):
    form = accountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('coachHome')
    content = {'form': form}
    return render(request, 'Jobs/coachCreate.html', content)

def childCreate(request):
    form = childForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('coachHome')
    content = {'form': form}
    return render(request, 'Jobs/coachChildSignups.html', content)
