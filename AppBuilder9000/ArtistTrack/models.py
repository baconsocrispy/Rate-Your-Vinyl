from django.db import models


# Create your models here.
class Song(models.Model):
    GENRE_CHOICES = (
        ('nu-metal', 'nu-metal'),
        ('metalcore', 'metalcore'),
        ('death metal', 'death metal'),
        ('rock', 'rock'),
        ('pop', 'pop'),
        ('classical', 'classical'),
        ('other', 'other'),
    )

    song_name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50, default=None, blank=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    year = models.IntegerField(default=None, blank=True)

    Songs = models.Manager()

    def __str__(self):
        return self.song_name


class Playlist(models.Model):
    playlist_name = models.CharField(max_length=50)
    playlist_description = models.TextField()
    playlist_songs = models.ManyToManyField(Song)

    Playlists = models.Manager()

    def __str__(self):
        return self.playlist_name















