from django.db import models

BOOKGENRE = [
    ('Science-Fiction', 'Science-Fiction'),
    ('Action and Adventure', 'Action and Adventure'),
    ('Fantasy', 'Fantasy'),
    ('History', 'History'),
    ('Horror', 'Horror'),
    ('Comic Book', 'Comic Book'),
    ('Mystery', 'Mystery'),
    ('Poetry', 'Poetry'),
]

GRADE = [
    ('1/5', '1/5'),
    ('2/5', '2/5'),
    ('3/5', '3/5'),
    ('4/5', '4/5'),
    ('5/5', '5/5'),
]


class AddBook(models.Model):
    book_genre = models.CharField(max_length=50, choices=BOOKGENRE),
    book_title = models.CharField(max_length=100, null=False),
    book_author = models.CharField(max_length=100, null=False),
    book_description = models.CharField(max_length=1000, null=False),
    book_score = models.CharField(choices=GRADE),

    AddBooks = models.Manager()

    def __str__(self):
        return self.book_title
