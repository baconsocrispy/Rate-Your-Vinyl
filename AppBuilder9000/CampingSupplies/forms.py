from django.forms import ModelForm
from .models import Tent, CookingTool, Pants, Coat

class campingsuppliesform(ModelForm):
    class Meta:
        model = Tent, CookingTool, Pants, Coat
        fields ="__all__"
