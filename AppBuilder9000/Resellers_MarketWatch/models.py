from django.db import models


# Create your models here.

Categories = [
    ('Electronics', 'Electronics'),
    ('Pet Supplies', 'Pet Supplies'),
    ('Toys & Games', 'Toys & Games'),
    ('Vehicles', 'Vehicles'),
    ('Apparel', 'Apparel'),
    ('Entertainment', 'Entertainment'),
    ('Family', 'Family'),
    ('Free Stuff', 'Free Stuff'),
    ('Garden & Outdoor', 'Garden & Outdoor'),
    ('Hobbies', 'Hobbies'),
    ('Home Goods', 'Home Goods'),
    ('Home Improvement Supplies', 'Home Improvement Supplies'),
    ('Musical Instruments', 'Musical Instruments'),
    ('Sporting Goods', 'Sporting Goods'),
]


class SearchResult(models.Model):
    url_link = models.URLField(primary_key=True, max_length=200)
    date = models.DateField(auto_now_add=False)
    list_price = models.DecimalField(decimal_places=2, max_digits=7)
    image = models.URLField(max_length=200)
    profit = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.date, self.image, self.list_price, self.profit, self.url_link

    Results = models.Manager()