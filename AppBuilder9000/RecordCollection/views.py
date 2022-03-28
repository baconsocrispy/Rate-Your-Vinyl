from django.shortcuts import render, redirect, get_object_or_404
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

#View Collection Page Req
def records_random(request):
    return render(request, 'RecordCollection/RecordCollection_Random.html')

def records_details(request, pk):
    details = get_object_or_404(Records, pk=int(pk))
    content = { 'details': details }
    return render(request, 'RecordCollection/RecordCollection_details.html', content)








