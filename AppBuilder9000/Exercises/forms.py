from django.forms import ModelForm
from .models import Exercises

class ExercisesForm(ModelForm):
    class Meta:
        model = Exercises
        fields = '__all__'