from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from .forms import RecordsForm
from .models import Records



#Home Page Req
def home(request):
    return render(request, 'RecordCollection/RecordCollection_home.html')

#View Collection Page Req
def records_view(request):
    records_db = Records.Records.all()
    content = {'records_db': records_db}
    return render(request, 'RecordCollection/RecordCollection_View.html', content)

#Add to Collection Page Req
def records_add(request):
    form = RecordsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('records_home')
    content = {'form': form}
    return render(request, 'RecordCollection/RecordCollection_Add.html', content)

#Random Album Page
def records_random(request):
    return render(request, 'RecordCollection/RecordCollection_Random.html')

#Album Details Page
def records_details(request, pk):
    details = get_object_or_404(Records, pk=pk)
    content = { 'details': details }
    return render(request, 'RecordCollection/RecordCollection_details.html', content)

#Edit Details
def records_edit(request, pk):
    item = get_object_or_404(Records, pk=pk)
    form = RecordsForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('records_details', pk=pk)
        else:
            print(form.errors)
    content = {'form': form}
    return render(request, 'RecordCollection/RecordCollection_edit.html', content)

#Model Specified for Delete View
def records_delete(request, pk):
    item = get_object_or_404(Records, pk=pk)
    content = {'item': item}
    if request.method == "POST":
        item.delete()
        return redirect('records_view')
    return render(request, 'RecordCollection/RecordCollection_Delete.html', content)












