import crispy_forms
from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'legend', 'gp', 'kills', 'tpt3']