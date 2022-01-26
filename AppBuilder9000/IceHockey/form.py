from django.forms import ModelForm
from .models import User, CreateAPlayer


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class CreateAPlayerForm(ModelForm):
    class Meta:
        model = CreateAPlayer
        fields = '__all__'
