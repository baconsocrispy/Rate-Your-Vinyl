from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .forms import ChampForm
from .models import Champions

def MMAHome(request):
    return render(request, 'MMAStats/MMA_home.html')

def MMACreate(request):
    form = ChampForm(data=request.POST or None)
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

def DeleteStat(request, pk):
    context = {}
    stat = get_object_or_404(Champions, pk=pk)

    if request.method == "POST":
        stat.delete()
        return redirect("MMA_Stats")

    return render(request, "MMAStats/MMA_delete.html", context)

def UpdateStat(request, pk):
    stat = Champions.objects.get(pk=pk)
    form = ChampForm(request.POST or None, instance=stat)
    if form.is_valid():
        form.save()
        return redirect('MMA_Stats')

    context = {'stat': stat, 'form': form}
    return render(request, 'MMAStats/MMA_update.html', context)