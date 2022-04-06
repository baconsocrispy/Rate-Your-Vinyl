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

FINISH_POSITION_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('DNF', 'DNF'),
]

# Create your models here.
class Team(models.Model):
    Team_Name = models.CharField(max_length=30, default="", unique=True, blank=False, null=False)
    Country = models.CharField(max_length=30, default="", blank=False, null=False)
    Engine_Manufacturer = models.CharField(max_length=30, choices=ENGINE_CHOICES, default="", blank=False, null=False)

    teams = models.Manager()

    def __str__(self):
        return self.Team_Name

class Race(models.Model):
    Round_Number = models.DecimalField(max_digits=2, decimal_places=0, default="", blank=False, null=False)
    Race_Location = models.CharField(max_length=30, default="", blank=False, null=False)
    Race_Type = models.CharField(max_length=30, choices=RACE_TYPE_CHOICES, default="Feature", blank=False, null=False)

    races = models.Manager()

    def __str__(self):
        return f"{self.Race_Location} - {self.Race_Type} Race"

class Driver(models.Model):
    Driver_Name = models.CharField(max_length=60, default="", unique=True, blank=False, null=False)
    Current_Team = models.ForeignKey(Team, on_delete=models.CASCADE, to_field="Team_Name")
    Age = models.DecimalField(max_digits=2, decimal_places=0, default="", blank=False, null=False)
    Nationality = models.CharField(max_length=30, default="", blank=False, null=False)

    drivers = models.Manager()

    def __str__(self):
        return self.Driver_Name

class Result(models.Model):
    Driver_Race_Key = models.CharField(max_length=100, default="", blank=False, null=False, unique=True)
    Driver_Name = models.ForeignKey(Driver, on_delete=models.CASCADE, to_field="Driver_Name")
    Current_Team = models.CharField(max_length=30, default="", blank=False, null=False)
    Race = models.ForeignKey(Race, on_delete=models.CASCADE)
    Finishing_Position = models.CharField(max_length=5, default="", choices=FINISH_POSITION_CHOICES, blank=False, null=False)
    Fastest_Lap = models.BooleanField()
    Points_Earned = models.DecimalField(max_digits=2, decimal_places=0, default="", blank=False, null=False)

    results = models.Manager()

    def __str__(self):
        return f"{self.Race} - {self.Driver_Name} finished in position {self.Finishing_Position} and scored {self.Points_Earned} points."