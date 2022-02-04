from django.forms import ModelForm
from .models import Motorcycle, Route


class MotorcycleForm(ModelForm):
    class Meta:
        model = Motorcycle
        fields = '__all__'


class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
