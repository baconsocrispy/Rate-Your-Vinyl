from django.db import models
from django.forms import ModelForm

#defining the movies model

class Movies(models.Model):
    FilmName = models.CharField(max_length=100)
    ReleaseYear = models.IntegerField(max_length=4, blank=True)
    StarNames = models.CharField(max_length=100, blank=True)
    DirectorName = models.CharField(max_length=60, blank=True)
    MovieSummary = models.TextField()

    #using the models manager to return the name of the course title
    objects = models.Manager()

    def __str__(self):
        return self.FilmName, self.ReleaseYear

class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['FilmName', 'ReleaseYear', 'StarNames', 'DirectorName', 'MovieSummary']
