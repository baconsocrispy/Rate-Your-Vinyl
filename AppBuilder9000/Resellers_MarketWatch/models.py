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


class WebScrape(models.Model):
    result_item = models.CharField(max_length=50, null=False)
    url = models.URLField(primary_key=True, max_length=200, null=False)
    date = models.DateField(auto_now_add=False, null=False)
    list_price = models.DecimalField(decimal_places=2, max_digits=7, null=False)
    image = models.URLField(max_length=200, blank=True)
    profit = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    WebScrape_db = models.Manager()


class InputForm(models.Model):
    result_item = models.ForeignKey(WebScrape, on_delete=models.CASCADE)
    search_item = models.CharField(max_length=50, null=False)
    min_price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    max_price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    profit_margin = models.DecimalField(max_digits=3, decimal_places=2, null=False)

    InputForm_db = models.Manager()












