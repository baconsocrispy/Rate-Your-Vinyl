from django.db import models

# creating initial model, this will allow us to input information in our
# database about
class Champions(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    defenses = models.IntegerField(default=0)
    p4p_rank = models.IntegerField(default=0)
    record = models.CharField(max_length=20)

    promotion = models.Manager()