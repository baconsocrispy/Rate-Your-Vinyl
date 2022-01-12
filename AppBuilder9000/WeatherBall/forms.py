from django.forms import ModelForm
from .models import User
from .models import Area

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email']

class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = 'STATES'

