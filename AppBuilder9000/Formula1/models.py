from django.db import models


ENGINE_CHOICES = {
    ('Ferrari', 'Ferrari'),
    ('Mercedes', 'Mercedes'),
    ('Red Bull', 'Red Bull'),
    ('Renault', 'Renault'),
}

RACE_TYPE_CHOICES = {
    ('Sprint', 'Sprint'),
    ('Feature', 'Feature'),
}

# Create your models here.
class Team(models.Model):
    Team_Name = models.CharField(max_length=30, default="", unique=True, blank=False, null=False)
    Country = models.CharField(max_length=30, default="", blank=False, null=False)
    Engine_Manufacturer = models.CharField(choices=ENGINE_CHOICES, default="", blank=False, null=False)

    teams = models.Manager()

    def __str__(self):
        return self.Team_Name

class Race(models.Model):
    Round_Number = models.DecimalField(max_digits=2, decimal_places=0, default="", blank=False, null=False)
    Race_Location = models.CharField(max_length=30, default="", blank=False, null=False)
    Race_Type = models.CharField(choices=RACE_TYPE_CHOICES, default="", blank=False, null=False)

    races = models.Manager()

    def __str__(self):
        return f"{self.Race_Location} - {self.Race_Type} Race"

class Driver(models.Model):
    Driver_Name = models.CharField(max_length=60, default="", unique=True, blank=False, null=False)
    Current_Team = models.ForeignKey(Team, on_delete=models.CASCADE, to_field=Team.Team_Name)
    Age = models.DecimalField(max_digits=2, decimal_places=0, default="", blank=False, null=False)
    Nationality = models.CharField(max_length=30, default="", blank=False, null=False)

    def __str__(self):
        return self.Driver_Name

class Results(models.Model):
    Driver_Name = models.ForeignKey(Driver, on_delete=models.CASCADE, to_field=Driver.Driver_Name)
    Current_Team = models.ForeignKey(Driver, on_delete=models.CASCADE, to_field=Driver.Current_Team)
    Race = models.ForeignKey(Race, on_delete=models.CASCADE)
    Finishing_Position = models.DecimalField(max_digits=2, decimal_places=0, default="", blank=False, null=False)
    Fastest_Lap = models.BooleanField()
    Points_Earned = models.DecimalField(max_digits=2, decimal_places=0, default="", blank=False, null=False)

    def __str__(self):
        return f"{self.Driver_Name} finished in position {self.Finishing_Position} and scored {self.Points_Earned} points."
