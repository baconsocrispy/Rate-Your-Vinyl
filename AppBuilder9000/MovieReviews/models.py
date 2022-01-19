from django.db import models

# Created Genre Choices
GENRE_CHOICES = {
    ('drama', 'drama'),
    ('comedy', 'comedy'),
    ('sci-fi', 'sci-fi'),
    ('romance', 'romance'),
    ('action-adventure', 'action-adventure'),
    ('classics', 'classics'),
    ('horror', 'horror'),
}
# Created Star Choices
STAR_CHOICES = {
    ('1 star', '1 star'),
    ('2 stars', '2 stars'),
    ('3 stars', '3 stars'),
    ('4 stars', '4 stars'),
    ('5 stars', '5 stars'),
}


class Movies(models.Model):
    movie_genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    movie_name = models.CharField(max_length=300, default="", blank=True, null=False)
    movie_description = models.TextField(max_length=5000, default="", blank=True)
    movie_rating = models.CharField(max_length=50, default="", blank=True)
    movie_director = models.CharField(max_length=100, default="", blank=True)
    movie_actor = models.CharField(max_length=100, default="", blank=True)
    movie_star_rating = models.CharField(max_length=100, choices=STAR_CHOICES)

    Movies = models.Manager()

    def __str__(self):
        return self.movie_name






