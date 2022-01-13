from django.forms import ModelForm
from .models import Airplane

class Airplanefom(ModelForm):
    class Meta:
        model = Airplane
        fields = '__all__'
