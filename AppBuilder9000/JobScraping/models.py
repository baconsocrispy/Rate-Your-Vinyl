from django.db import models

# Create your models here.

stackChoices = {
    ('Full-Stack','Full-Stack'),
    ('Front-End','Front-End'),
    ('Back-End','Back-End'),
    ('Unknown','Unknown'),
}

class Jobs(models.Model):
    title = models.CharField(max_length=60, default="", blank=True)
    stack = models.CharField(max_length=15, choices=stackChoices)

    def __str__(self):
        return self.title