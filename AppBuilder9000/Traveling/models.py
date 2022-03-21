from django.db import models

class Traveler(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 254)


    Travelers = models.Manager()



    def __str__(self):
        return self.first_name + ' ' + self.last_name

reason = [('Vacations','Vacations'), ('Business', 'Business')]


class Place(models.Model):
    Place = models.CharField(max_length = 100)
    Departure_date = models.DateField()
    Departure_time = models.TimeField()
    Price = models.DecimalField(default=0.00, max_digits=10000, decimal_places = 2)


    Places = models.Manager()


class Schedule(models.Model):
    Reason = models.CharField(max_length = 50, choices= reason)


