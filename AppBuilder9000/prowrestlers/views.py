from django.shortcuts import render, redirect, get_object_or_404
from .forms import wrestlerform
from models import Wrestler

from .models import Wrestler

# Create your views here.
def wrestlers_home(request):
    return render(request, 'Prowrestlers/ProWrestling_home.html')

def add_prowrestler(request):
    form = wrestlerform(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('wrestlers_home')
    else:
        print(form.errors)
        form = wrestlerform
        context = {'form': form}
    return render(request, 'Prowrestlers/ProWrestling_createpage.html', context)

def prowrestler_details(request, pk):
    prowrestler_detail = get_object_or_404(Wrestler, pk=pk)
    return render(request, 'Prowrestlers/ProWrestling_details.html', {'prowrestler_detail': prowrestler_detail})