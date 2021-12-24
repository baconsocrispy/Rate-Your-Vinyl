from django.db import models

# Create your models here.

# Creates user account
class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    # PASSWORD - use form widget=password_input in forms section
        # Above syntax allows password value anonymity (i.e. password = *******)
    password = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return self.username


# Allows authorized users to set initial goals
class Goals(models.Model):

    # CHOICES SECTION================================
    Mile_Dur = [
        ("2wks", "By 2-Weeks"),
        ("1mo", "By 1-Month"),
        ("6wks", "By 6-Weeks"),
        ("2mo", "By 2-Months"),
        ("3mo", "By 3-Months"),
        ("6mo", "By 6-Months"),
    ]

    Type_Of_Goal = [
        ("skill", "Gain New Skill"),
        ("improve", "Improve Existing Skill"),
        ("break", "Break Bad Habit"),
        ("unsure", "Not Sure"),
    ]
    # END SECTION============================================================================

    # COLUMNS FOR DATABASE=====================================================
    user = models.ForeignKey('Register', default="", on_delete=models.CASCADE)
    Goal_Type = models.CharField(max_length=25, choices=Type_Of_Goal)
    Your_Goal = models.CharField(max_length=100)
    Reason = models.TextField(max_length=350)
    Target_Range = models.CharField(max_length=20, choices=Mile_Dur)

    objects=models.Manager()

    def __str__(self):
        return self.Goal_Type

class Progress(models.Model):

    # CHOICES SECTION ========================
    Hours_Spent = [
        ("lt1", "<1"),
        ("1to3", "1-3"),
        ("4to6", "4-6"),
        ("gt6", "6+"),
    ]
    # END SECTION ================================================================

    Goal = models.ForeignKey(Goals, default="", on_delete=models.CASCADE)
    Daily_Hours_Spent = models.CharField(max_length=5, choices=Hours_Spent)
    Task_Completed = models.CharField(max_length=200)
    Any_Challenges = models.CharField(max_length=200)
    Other_Thoughts = models.CharField(max_length=200)

    objects = models.Manager()

class Diary(models.Model):
    username = models.ForeignKey(Register, default="", on_delete=models.CASCADE)
    Entry_Date = models.DateTimeField(auto_now=True)
    Entry = models.TextField(max_length=400)

    objects = models.Manager()

    def __str__(self):
        return self.Entry_Date


