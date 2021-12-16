from django.forms import ModelForm
from AppBuilder9000.BasketballStats.models import Players


class PlayersForm(ModelForm):
    class Meta:
        model = Players
        fields = '__all__'
