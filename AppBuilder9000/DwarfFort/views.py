from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Fbeast
from .forms import FbeastForm

# Story 1 - Build Basic App
def dfort_home(request):
    beast = Fbeast.Fbeasts.all().order_by('pk')
    context = {'beast' : beast}
    return  render(request, 'DwarfFort/dfort_home.html', context)

# Story 2 - Build Model
def dfort_create(request):
    form = FbeastForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dfort_home')
    context = {'form': form}
    return  render(request, 'DwarfFort/dfort_create.html', context)

# Story 3 - Display Database

def dfort_display(request):
    beast = Fbeast.Fbeasts.all().order_by("title")

    # builds collection of models from beast and limits display to 5 at a time
    paginator = Paginator(beast, 5)
    page = request.GET.get('page')
    beastpage = paginator.get_page(page)


    context = {'beastpage' : beastpage}

    return render(request, 'DwarfFort/dfort_display.html', context)

# Display search results

def dfort_search(request):
    if request.method == "POST":
        name = request.POST.get('usr_query')
        beast = Fbeast.Fbeasts.filter(name=name)
        context = { 'name' : name, 'beast' : beast}

        return render(request, 'DwarfFort/dfort_search.html', context)

# Story 4 - Details Page

def dfort_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Fbeast, pk=pk)
    form = FbeastForm(data=request.POST or None, instance=item)
    beast = Fbeast.Fbeasts.all().order_by('pk')

    # Dictionary for visualizer
    # Builds a different dictionary to display different species types
    match item.species:


#        case : TEMPLATE

#            beast_body = {'top1': '#######',
#                          'top2': '#######',
#                          'mid': '#######',
#                          'bot1': '#######',
#                          'bot2': '#######'}

        case 'reptilian':

                    beast_body = {'top1': ' {(")} ',
                                  'top2': '_--+--_',
                                  'mid': ' / |   | \ ',
                                  'bot1': '[  |__|  ]',
                                  'bot2': ' _/  \_ '}

        case 'avian':

            beast_body = {'top1': '  }B>  ',
                          'top2': ' o-^-o ',
                          'mid': '[|   |]',
                          'bot1': '[ \_/ ]',
                          'bot2': '  | |  '}


        case _:
            # debug to check case being met
            print('none')

            beast_body = {'top1': '  ___  ',
                          'top2': ' ( ~ ) ',
                          'mid': '(  0  )',
                          'bot1': '(_____)',
                          'bot2': ' |   | '}

    context = {'form': form, 'item': item, 'beast_body': beast_body, 'beast' : beast}

    return render(request, 'DwarfFort/dfort_details.html', context)

''' For CRUD use later
def dfort_details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Fbeast, pk=pk)
    form = FbeastForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('DwarfFort/dfort_home.html')
        else:
            print(form.errors)
    else:
        return render(request, 'DwarfFort/dfort_details.html', {'form': form})
'''