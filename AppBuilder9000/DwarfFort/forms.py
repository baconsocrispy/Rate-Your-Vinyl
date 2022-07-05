from django.forms import ModelForm
from .models import Fbeast


class FbeastForm(ModelForm):
    class Meta:
        model = Fbeast
        fields = '__all__'