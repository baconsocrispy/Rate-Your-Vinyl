from django import forms
from .models import TrackApp

class TrackApp(forms.ModelForm):
    class Meta:
        model = TrackApp
        fields = "__all__"





