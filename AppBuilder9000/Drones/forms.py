from django.forms import ModelForm
from .models import Drone


class DroneForm(ModelForm):
    class Meta:
        model = Drone
        fields = '__all__'


