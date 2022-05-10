from django.db import models

# Create your models here.
TYPE_GRADE = {
    ('K-1st','K-1st'),
    ('2nd-3rd','2nd-3rd'),
    ('4th-5th','4th-5th'),
    ('6th-7th','6th-7th'),
}

class account(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=30)
    coach_Grade = models.CharField(max_length=10, choices=TYPE_GRADE, default='please choose')



    accounts = models.Manager()

    def __str__(self):
        return self.name

class singupChild(models.Model):
    child_Name = models.CharField(max_length=60)
    grade = models.CharField(max_length=10, choices=TYPE_GRADE)
    Parent_Name = models.CharField(max_length=60)
    Parent_Phone = models.CharField(max_length=60)
    Parent_Email = models.CharField(max_length=60)

    singupChild = models.Manager()

    def __str__(self):
        return self.child_Name