from django.forms import ModelForm
from .models import Person, SelectPerson


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


class SelectPersonForm(ModelForm):
    class Meta:
        model = SelectPerson
        fields = '__all__'
