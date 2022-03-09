from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, ComparedPerson, SelectPerson
from .forms import PersonForm, SelectPersonForm
from django.views import generic
from django.http import HttpResponse


#def personality_home(request):
#    return render(request, 'Personality/personality_home.html')

def personality_home(request):
    form = SelectPersonForm(data=request.POST or None)
    print("I'm home")
    print(form)
    if request.method == 'POST':
        print("sent")
        pk = request.POST['person']
        print("This is pk:")
        print(pk)
        return
    content = {'form': form}
    return render(request, 'Personality/personality_home.html', content)


#def personality_create(request):
#    return render(request, 'Personality/personality_create.html')

def personality_create(request):
    form = PersonForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/Personality/')
    content = {'form': form}
    return render(request, 'Personality/personality_create.html', content)


#def personality_compare(request):
#    return render(request, 'Personality/personality_compare.html')

def personality_compare(request):
    data = Person.Persons.all()
    pers = {"person": data}

#    content = {'person': person}
    return render(request, 'Personality/personality_compare.html', pers)


#class PersonalityDetailView(generic.DetailView):
#    print("details")
#    pers = Person.Persons.all()
#    form = PersonForm(data=pers or None)
#    model = Person
#    template_name = 'Personality/personality_details.html'

def personality_details(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'Personality/personality_details.html', {'person': person})


def personality_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)

    def deleteAccount():
        print("hey there")
        person.delete

    deleteMe = deleteAccount

    form = PersonForm(initial={'name': person.name, 'age': person.age, 'sex': person.sex,
                               'o_average_score': person.o_average_score, 'c_average_score': person.c_average_score,
                               'e_average_score': person.e_average_score, 'a_average_score': person.a_average_score,
                               'n_average_score': person.n_average_score})
    if request.method == 'POST':
        print("yep")
        if form.is_valid():
            print("form saved")
            form.save()
            return redirect('/Personality/')
    content = {'form': form, 'deleteMe': deleteMe}
    return render(request, 'Personality/personality_edit.html', content)
