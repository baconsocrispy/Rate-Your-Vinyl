from django.db import models



# To provide choices for inpput user
Manufacture = [
    ('Boeing', 'Boeing'),
    ('Airbus', 'Airbus'),
    ('Bombardier', 'Bombardier'),
    ]

#to provide choices for inpput user

Type = [
    ('Widebody', 'Widenody'),
    ('Narrowbody', 'Narrowbody'),
]

#to provide choices for inpput user

Propulsion = [
    ('Jet', 'Jet'),
    ('Turboprop', 'Turboprop'),
]

class Airplane(models.Model):
    Manufacture = models.CharField(max_length=20, default='', choices=Manufacture)
    Size = models.CharField(max_length=20, default='', choices=Type)
    Propulsion = models.CharField(max_length=20, default='', choices=Propulsion)
    Model = models.CharField(max_length=20, default='')

    Plane = models.manager

    def __str__ (self):
        return self.Manufacture