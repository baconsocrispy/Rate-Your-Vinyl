from django.db import models


class VideoReviews(models.Model):
    GameName = models.CharField(max_length=60)
    GameGenre = models.CharField(max_length=60)
    GameReview = models.TextField(max_length=700)
    GameRating = models.IntegerField(default=0)

    objects = models.Manager()

    Rating = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    )
