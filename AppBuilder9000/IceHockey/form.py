from django.forms import ModelForm
from .models import Profile


class UserForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'favorite_team', 'favorite_player')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'favorite_team': 'Favorite Team',
            'favorite_player': 'Favorite NHL Player',
        }


