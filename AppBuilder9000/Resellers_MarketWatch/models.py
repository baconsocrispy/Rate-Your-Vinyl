from django.db import models



# Create your models here.

Categories = [
    ('Electronics', 'Electronics'),
    ('Pet Supplies', 'Pet Supplies'),
    ('Vehicles', 'Vehicles'),
]


class WebScrape(models.Model):
    category = models.CharField(max_length=50, choices=Categories)
    url = models.URLField(primary_key=True, max_length=200)
    date = models.DateField(auto_now_add=False)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    imageUrl = models.URLField(max_length=200)
    profit = models.DecimalField(max_digits=5, decimal_places=2)

    WebScrape_db = models.Manager()

    def __str__(self):
        return self.category












