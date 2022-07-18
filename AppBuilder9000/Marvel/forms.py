from django.forms import ModelForm
from .models import Character, Comment


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = "__all__"


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
