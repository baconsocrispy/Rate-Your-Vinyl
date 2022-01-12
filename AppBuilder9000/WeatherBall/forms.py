from django.forms import ModelForm
from .models import Users
from .models import Area

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = '__all__'

