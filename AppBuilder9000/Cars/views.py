from django.shortcuts import render

def Cars(request):
    return render(request, 'CarsHome.html')


def Car_Create(request):
    form = DescriptionForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        result = form.save()
        return redirect('Add_Car')
    else:
        return render(request, 'templates/CarCreate.html', {'form': form})