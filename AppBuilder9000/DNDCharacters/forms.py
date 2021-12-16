from django.forms import ModelForm
from .models import Characters

class CharcterForm(ModelForm):
    class Meta:
        model = Characters
        fields = '__all__'
