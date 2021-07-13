from django.shortcuts import render
from .models import PreciousMetalsItem
from .forms import MetalForm


# Create your views here.
def home(request):
    return render(request, 'PreciousMetals_home.html', {})

def addMetalItem(request):
    form = MetalForm(data=request.POST or None)
        if form.is_valid():
            from.save()
            return redirect
        pk = request.POST['PreciousMetalsItem']
        return PreciousMetalsItem(request, pk)
        content = {'form': form}
        return render(request, 'PreciousMetals_home.html', content)