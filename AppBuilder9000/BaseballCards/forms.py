from django.forms import ModelForm
from .models import BaseballCard

class BaseballCardForm(ModelForm):
    class Meta:
        model = BaseballCard
        fields = '__all__'

