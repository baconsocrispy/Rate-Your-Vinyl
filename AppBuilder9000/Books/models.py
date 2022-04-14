from django.db import models

BOOK_GENRE = [
    ('Science-Fiction', 'Science-Fiction'),
    ('Action and Adventure', 'Action and Adventure'),
    ('Fantasy', 'Fantasy'),
    ('History', 'History'),
    ('Horror', 'Horror'),
    ('Comic Book', 'Comic Book'),
    ('Mystery', 'Mystery'),
    ('Poetry', 'Poetry'),
]


# instantiating my model
class AddBook(models.Model):
    book_genre = models.CharField(max_length=100, choices=BOOK_GENRE)
    book_title = models.CharField(max_length=100, null=False)
    book_author = models.CharField(max_length=100, null=False)
    book_description = models.TextField(max_length=500, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.book_title
