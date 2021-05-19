from django.forms import ModelForm, TextInput
from .models import Song
from django import forms


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

#API

class SearchForm(forms.Form):
   artist = forms.CharField(max_length=100)
   title = forms.CharField(max_length=100)




