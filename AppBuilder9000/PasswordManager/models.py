from django.db import models


# Create your models here:
PasswordTypes = [('Personal', 'Personal'), ('Work', 'Work'), ('Combo', 'Combo'), ('Other', 'Other')]


class NewPasswords(models.Model):
    type = models.CharField(maxlength=8, choices=PasswordTypes)
    creation_date = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=True)
    website = models.Charfield(maxlength=100)
    email = models.EmailField(max_length=120)
    username = models.CharField(maxlength=60)
    password = models.CharField(max_length=60)
    favorite = models.BooleanField(default=False)




