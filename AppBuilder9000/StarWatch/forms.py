from django.forms import ModelForm
from .models import celestialObject


class form_addObject(ModelForm):
    class Meta:
        model = celestialObject
        fields = '__all__'