from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConvertForm
from .models import Convert
import requests

# Create your views here.
def home(request):
    return render(request, "RecipeConvert/RecCon_home.html")

def convert(request):
    form = ConvertForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('RecCon_home')
    # else:
    #     print(form.errors)
    #     form = ConvertForm()
    context = {
        'form': form,
    }
    return render(request, "RecipeConvert/RecCon_convert.html", context)
