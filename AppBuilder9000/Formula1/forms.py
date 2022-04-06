from django import forms
from django.forms import ModelForm, Select, CheckboxInput
from .models import Result

class ResultForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Driver_Name'].label = ''
        self.fields['Driver_Name'].empty_label = 'Select a Driver'
        self.fields['Race'].label = ''
        self.fields['Race'].empty_label = 'Select a Race'
        self.fields['Fastest_Lap'].label = 'Fastest Lap?'


    class Meta:
        model = Result
        fields = ['Driver_Name', 'Race', 'Finishing_Position', 'Fastest_Lap']
        widgets = {
            'Driver_Name': Select(attrs={
                'class': 'form-dropdown'
            }),
            'Race': Select(attrs={
                'class': 'form-dropdown'
            }),
            'Finishing_Position': Select(attrs={
                'class': 'small-form-dropdown'
            }),
            'Fastest_Lap': CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }