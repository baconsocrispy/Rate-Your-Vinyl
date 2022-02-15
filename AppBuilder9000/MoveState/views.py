from django.shortcuts import render, get_object_or_404, redirect

from .form import movestateForm
from .models import Movestate


def movestate_home(request):
    return render(request, "MoveState/movestate_home.html")


def add_state(request):
    form = movestateForm(data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movestate_home')
    else:
        print(form.errors)
        form = movestateForm()
    context = {
        'form': form,
    }
    return render(request, 'MoveState/add_state.html', context)


def list_state(request):
    list = Movestate.Movers.all()
    return render(request, 'MoveState/list_state.html', {'list': list})


def movestate_details(request, pk):
    details = get_object_or_404(Movestate, pk=pk)
    context = {'details': details}
    return render(request, 'MoveState/movestate_details.html', context)


def movestate_delete(request, pk):
    item = get_object_or_404(Movestate, pk=pk)
    form = movestateForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        item.delete()
        return redirect('list_state')
    context = {"item": item, 'form': form}
    return render(request, "MoveState/movestate_delete.html", context)


def movestate(data, instance):
    pass


def movestate_edit(request, pk):
    item = get_object_or_404(Movestate, pk=pk)
    form = movestateForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('list_state')
        else:
            print(form.errors)
    else:
        return render(request, 'MoveState/movestate_edit.html', {'form': form})


def movestate_history(request):
    champion_list = []
    page = requests.get("https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_net_migration")
    soup = BeautifulSoup(page.content, 'html.parser')
    previous_state = soup.find('section', class_='post__content text-article')
    champions = previous_state.find_all('tr')[1:]
    for tr in movestate:
        td = tr.find_all('td')
        row = [i.text for i in td]
        cells = row
        champion_list.append(cells)
    context = {'movestate_list': champion_list}
    return render(request, 'MoveState/movestate_history.html', context)