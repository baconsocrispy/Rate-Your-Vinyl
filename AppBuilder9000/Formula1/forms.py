from django.forms import ModelForm
from .models import Result

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = ['Driver_Name', 'Race', 'Finishing_Position', 'Fastest_Lap']