from django.db import models


# Create your models here.
class BookEntry(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField(max_length=1000)

    BookEntrys = models.Manager()

    def __str__(self):
        return self.title



