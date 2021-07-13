from django.forms import ModelForm
from .models import Defensive_Stats


class Def_Stats_Form(ModelForm):
    class Meta:
        model = Defensive_Stats
        fields = '__all__'
