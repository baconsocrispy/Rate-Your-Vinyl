from django.forms import ModelForm
from .models import WebScrape, UserLogin

# This class needs to be renamed

    # created a form class


class WebscrapeForm(ModelForm):
    class Meta:
        model = WebScrape
        fields = '__all__'


class UserLoginForm(ModelForm):
    class Meta:
        model = UserLogin
        fields = '__all__'
