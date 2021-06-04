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






# class Musician(models.Model):
#     INSTRUMENT_CHOICES = {
#         ('bass guitar', 'bass guitar'),
#         ('drummer', 'drummer'),
#         ('guitar', 'guitar'),
#         ('vocals', 'vocals'),
#     }
#     first_name = models.CharField(max_length=50, help_text='first name')
#     last_name = models.CharField(max_length=50, help_text='last name')
#     instrument = models.CharField(max_length=50, choices=INSTRUMENT_CHOICES)
#
#     objects = models.Manager()
#
#     def __str__(self):
#         full_name = self.first_name + ' ' + self.last_name
#         return full_name







