from django.forms import ModelForm
from .models import Location, thingsToDo, Accommodations

# shortcut template
# ModelForm queries everything from dB all at once


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class thingsToDoForm(ModelForm):
    class Meta:
        model = thingsToDo
        fields = '__all__'


class AccommodationsForm(ModelForm):
    class Meta:
        model = Accommodations
        fields = '__all__'