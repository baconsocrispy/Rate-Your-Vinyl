from django import forms
from .models import Species

class speciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = "__all__"