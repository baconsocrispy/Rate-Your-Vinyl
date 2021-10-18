from django.forms import ModelForm
from .models import RockLoc

class RockForm(ModelForm):
    class Meta:
        model = RockLoc
        fields = '__all__'