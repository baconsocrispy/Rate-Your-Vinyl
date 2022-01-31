from django.forms import ModelForm
from .models import Create


class CreateForm(ModelForm):
    class meta:
        model = Create
        fields = '__all__'
