from django import forms

from .models import Wrestler


class wrestlerform(forms.ModelForm):
    class meta:
        model = Wrestler
        fields = '__all__'
