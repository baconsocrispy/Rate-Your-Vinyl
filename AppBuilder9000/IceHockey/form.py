from django.forms import ModelForm
from django import forms
from .models import Profile, FavPlayer


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


class PlayerForm(forms.Form):
    player_name = forms.CharField(max_length=50)
    player_number = forms.IntegerField(max_value=99, min_value=1)
    player_position = forms.CharField(max_length=1)
