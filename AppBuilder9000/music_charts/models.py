from django.db import models


# These wll be the parent options for what the user wants to find
# info on
music_type = (
    ('Song', 'Song'),
    ('Artist', 'Artist'),
    ('Album', 'Album'),
)
# creating a class named charts to resemble records you would find
# in a chart
class Charts(models.Model):
    selection = models.CharField(max_length=50, choices=music_type)
    artist_name = models.CharField(max_length=50, default='enter artist', blank=True, null=False)
    song_title = models.CharField(max_length=50, default='enter song title', blank=True, null=False)
    album_title = models.CharField(max_length=50, default='enter album title', blank=True, null=False)
    rank_this_week = models.DecimalField(max_digits=200, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.selection
