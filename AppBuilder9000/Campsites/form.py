from django.forms import ModelForm
from .models import CampSites, Location


class CampsitesForm(ModelForm):
    class Meta:
        model = CampSites
        model = Location
        fields = '__all__'
