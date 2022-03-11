from django.forms import ModelForm
from django import forms
from .models import Person, SelectPerson


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class SelectPersonForm(ModelForm):
    class Meta:
        model = SelectPerson
        fields = '__all__'


class JobSearchForm(forms.Form):
    query = forms.CharField(label='Search:', max_length=50)
    location = forms.CharField(label='Location:', max_length=50)