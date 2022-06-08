from django.db import models

# Create your models here.

stackChoices = {
    ('Full-Stack','Full-Stack'),
    ('Front-End','Front-End'),
    ('Back-End','Back-End'),
    ('Unknown','Unknown'),
}

yesNo = {
    ('yes', 'yes'),
    ('no', 'no'),
}


class Jobs(models.Model):
    title = models.CharField(max_length=60, default="")
    company = models.CharField(max_length=30, default="")
    stack = models.CharField(max_length=15, choices=stackChoices)
    startup = models.CharField(max_length=3, choices=yesNo)
    location = models.CharField(max_length=30)
    exp_required = models.CharField(max_length=30)
    pay = models.CharField(max_length=30)

    objects = models.Manager()

    def __str__(self):
        return self.title