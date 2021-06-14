from django.db import models
class Film(models.Model):
    Name_of_film = models.CharField(max_length=100)
    Year_of_film = models.IntegerField()
    Film_star_names = models.CharField(max_length=100)
    Director_names = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.Name_of_film


