from django.forms import ModelForm
from django import forms
from .models import Song, Playlist


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
        #allows me to use bootstrap to style the form
        widgets = {
            'song_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Song Name'}),
            'artist': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Artist'}),
            'album': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Album'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            # 'playlist': forms.Select(attrs={'class': 'form-control'}),
        }


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        fields = ['playlist_name', 'playlist_description', 'playlist_songs']

        playlist_name = forms.CharField()
        playlist_description = forms.CharField()
        playlist_songs = forms.ModelMultipleChoiceField(queryset=Song.Songs.all())

        widgets = {
            'playlist_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Playlist Name'}),
            'playlist_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'a description about your playlist'}),
            'playlist_songs': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
