from django.forms import ModelForm
from AppBuilder9000.BasketballStats.models import Players


class PlayersForm(ModelForm):
    class Meta:
        model = Players
        fields = ['name', 'seasons_played', 'mvp_awards', 'championships', 'hall_of_fame']
