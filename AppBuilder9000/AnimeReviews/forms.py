from django.forms import ModelForm
from .models import Anime


class NewAnime(ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'
