from django.shortcuts import render
from .models import PreciousMetalsItem
from .forms import MetalForm


# Create your views here.
def home(request):
    form = MetalForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['PreciousMetalsItem']
        return PreciousMetalsItem(request, pk)
    content = {'form': form}
    return render(request, 'PreciousMetals_home.html', content)
