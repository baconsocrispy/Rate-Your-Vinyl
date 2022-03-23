from django.forms import ModelForm
from .models import House


class HouseForm(ModelForm):
    class Meta:
        model = House
        # This indicates that we want all model fields in the form:
        fields = '__all__'
