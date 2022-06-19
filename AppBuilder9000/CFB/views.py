from django.shortcuts import render, redirect
from .forms import AddFanForm
from .models import AddFan

def CFB_Home(request):
    return render(request, 'CFB/CFB_Home.html')

def CFB_AddFan(request):
    form = AddFanForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('..')
    content = {'form': form}
    return render(request, 'CFB/CFB_CreateFan.html', content)

def CFB_FanList(request):
    fan_list = AddFan.objects.all()
    content = {'fan_list': fan_list}
    return render(request, 'CFB/CFB_DisplayFans.html', content)

