from django.shortcuts import render


#Home Page Req
def home(request):
    return render(request, 'RecordCollection/RecordCollection_home.html')

#View Collection Page Req
def records_view(request):
    return render(request, 'RecordCollection/RecordCollection_View.html')

#Add to Collection Page Req
def records_add(request):
    return render(request, 'RecordCollection/RecordCollection_Add.html')

#View Collection Page Req
def records_random(request):
    return render(request, 'RecordCollection/RecordCollection_Random.html')






