from django.shortcuts import render, get_object_or_404, redirect
from .models import MyShows
from .forms import ShowForm


def home(request):
    return render(request, 'VP_TrackShows/home.html',)


def admin_console(request):
    shows = MyShows.objects.all()
    return render(request, 'VP_TrackShows/shows_page.html', {'shows': shows})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(MyShows, pk=pk)
    form = ShowForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'VP_TrackShows/present_show.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(MyShows, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    context = {"item": item,}
    return render(request, "VP_TrackShows/confirm_delete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = ShowForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console')
    else:
        return redirect('admin_console')


def create_record(request):
    form = ShowForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        form = ShowForm()
    context = {
        'form': form,
    }
    return render(request, 'VP_TrackShows/create_record.html', context)
