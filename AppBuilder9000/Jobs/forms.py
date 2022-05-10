from django.forms import ModelForm
from .models import account, singupChild


class accountForm(ModelForm):
    class Meta:
        model = account
        fields = '__all__'

class childForm(ModelForm):
    class Meta:
        model = singupChild
        fields = '__all__'