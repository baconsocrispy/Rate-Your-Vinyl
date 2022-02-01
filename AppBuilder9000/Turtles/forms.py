from django.forms import ModelForm
from .models import Turtles


class CreateForm(ModelForm):
    class Meta:
        model = Turtles
        fields = '__all__'
