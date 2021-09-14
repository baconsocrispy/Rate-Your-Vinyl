from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConvertForm
from .models import Convert
import requests

# Create your views here.
def home(request):
    return render(request, "RecipeConvert/RecCon_home.html")

def convert(request):
    if request.method == "POST":
        form = ConvertForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('RecCon_home')
    else:
        form = ConvertForm()
        context = {
            'form': form,
        }
        return render(request, "RecipeConvert/RecCon_convert.html", context)

def myrecipesList(request):
    dataset = Convert.objects.all()
    return render(request, "RecipeConvert/RecCon_myrecipes.html", {'dataset': dataset})

def myrecipesDetail(request,_id):
    try:
        data = ConvertForm.objects.get(id = _id)
    except ConvertForm.DoesNotExist:
        raise Http404('Data does not exist')

    return  render(request, "RecipeConvert/RecCon_myrecipes.html",{'data':data})

