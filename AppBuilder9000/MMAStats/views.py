from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChampForm
from .models import Champions

def MMAHome(request):
    return render(request, 'MMAStats/MMA_home.html')

def MMACreate(request):
    form = ChampForm (data=request.POST or None)
    # if form data is valid
    if request.method=='POST':
        if form.is_valid():
            # save form data to our model
            form.save()
            return redirect('MMA_Create')

    context = {'form': form}
    return render(request, "MMAStats/MMA_create.html", context)

def MMAStats(request):
    return render(request, 'MMAStats/MMA_stats.html')

def DisplayStats(request):
    champion_stats = Champions.objects.all().order_by("p4p_rank")
    context = {'champion_stats': champion_stats}
    return render(request, 'MMAStats/MMA_stats.html', context)

def DisplayDetails(request, pk):
    stat = get_object_or_404(Champions, pk=pk)
    context = {'stat': stat}
    return render(request, 'MMAStats/MMA_details.html', context)