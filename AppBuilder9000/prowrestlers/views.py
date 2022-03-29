from django.shortcuts import render

# Create your views here.
def wrestlers_home(request):
    return render(request, 'Prowrestlers/ProWrestling_home.html')

def add_prowrestler(request):
    form = ProWrestler_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('wrestlers_home')
    else:
        print(form.errors)
        form = Prowrestler_Form
        context = {'form': form}
    return render(request, 'ProWrestling_create.html', context)