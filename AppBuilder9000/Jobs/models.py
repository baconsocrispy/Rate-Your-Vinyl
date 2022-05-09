from django.db import models

# Create your models here.
TYPE_CHOICES = {
    ('Underwater Basket Weaving','Underwater Basket Weaving'),
    ('Junior Developer','Junior Developer'),
    ('Icecream taste-tester','Icecream tastetester'),
    ('Mechanical Engineer','Mechanical Engineer'),
}

class Account(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=30)
    receive_updates = models.BooleanField()


    Accounts = models.Manager()

    def __str__(self):
        return self.name