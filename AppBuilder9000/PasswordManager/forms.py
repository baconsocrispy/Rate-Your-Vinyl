from django.forms import ModelForm
from.models import NewPasswords


class NewPasswordsForm(ModelForm):
    class Meta:
        model = NewPasswords
        fields = '__all__'