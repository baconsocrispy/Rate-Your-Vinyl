from django.forms import ModelForm
from .models import Jobs

class JobsForm(ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'