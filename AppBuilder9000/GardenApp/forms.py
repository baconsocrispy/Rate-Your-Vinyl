from django import forms
from .models import Planner, zone_type
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class PlannerForm(forms.ModelForm):
    Growing_Year = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'current year i.e. 2021'}))
    Growing_Zone = forms.ChoiceField(choices= zone_type)
    Sowing_Time_Frame = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'months i.e. March-April or soil temp'}))
    Harvest_Notes = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'time, plant size, and how to harvest'}))
    General_Care_Notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'sunshine/shade, watering needs, nutrient needs, weeding protocol'}))

    class Meta:
        model = Planner
        fields = '__all__'

    def __init__(self, *args, **kwargs):    # overide forms.ModelForm
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('save_plan', 'Save Garden Plan'))
        self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn btn-dnager'))


