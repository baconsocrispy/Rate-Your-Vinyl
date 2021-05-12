from django.forms import ModelForm, TextInput
from .models import Song


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

