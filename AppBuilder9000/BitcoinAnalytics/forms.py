from django.forms import ModelForm
from .models import Competitor


class CompetitorForm(ModelForm):
    class Meta:
        model = Competitor
        fields = '__all__'

