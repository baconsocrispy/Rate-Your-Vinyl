# 1. Create your models here.
    # 0 prior to this, set up the settings.py, base.html, home.html, some css, urls, views.
    # Models.py is How data is represented, accessed, manipulated. defined/represented by Python classes, automated by Django.
    # the class is called model. it drives the dB data.
    # this should be in the app directory folder, RevitFunctions is an app (there can be more than 1 app)
    # each app should have it's own __init__.py, manage.py, settings.py, urls.py
    # go back to the directory where manage.py resides > type: python manage.py makemigrations >
    # then migrate
    # since created classes for forms, next to create the forms.py
    # models.py: Here you can store the application’s data models.
#This is where you specify the entities and relationships between data.
    #dB schema
#https://docs.djangoproject.com/en/3.2/topics/db/models/
# next 1A. register the application in admin.py
# need to migrate after any changes to dB.

from django.db import models

# Create your models here = Create all Classes here
# Story2, Step1: Create your model and add a migration, make sure to plan out all the categories you want to track for your object. Include an objects manager for accessing the database.


rvt_level_choice = {
    ('Novice','Novice' ),
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advance', 'Advance'),
}

job_category_choice = {
    ('Designer', 'Designer'),
    ('Production', 'Production'),
    ('Administration', 'Administration'),
    ('Project Lead', 'Project Lead'),
}

rvt_category_choice = {                                                 # drop menu for types. dictionary object, tuple.
    ('Revit Basic', 'Revit Basic'),
    ('Revit Maintenance', 'Revit Maintenance'),
    ('Revit Troubleshoot', 'Revit Troubleshoot'),
    ('Revit Collaboration', 'Revit Collaboration'),
    ('Revit Plug-ins', 'Revit Plug-ins'),
    ('Revit Modeling', 'Revit Modeling'),
    ('Revit Documentation', 'Revit Documentation'),
    ('BIM360', 'BIM360'),
}


class User(models.Model):
    email = models.CharField(max_length=80, default="",                 # start off as empty: default = "", but the form can't be blank blank=True
                                 blank=True, null=False)
    rvt_level = models.CharField(max_length=50, choices=rvt_level_choice)
    job_category = models.CharField(max_length=50, choices=job_category_choice)
                                                                        # NOT utilized here: IntField does not have max_length - always check doc for more info

    Users = models.Manager()                                         # use the models that we involked. Must be within the class.


                                                                        # basic schema of Product, must register the app in admin file for it to show on browser.
class RvtFunction(models.Model):                                       # Model is the class
    rvt_title = models.CharField(max_length=80, default="",
                                 blank=True, null=False)                # start off as empty: default = "", but the form can't be blank blank=True
    rvt_description = models.TextField(max_length=300, default="",
                                       blank=True)                      # TextField allow for many texts
    rvt_category = models.CharField(max_length=50,                      # fields, what are the restrictions, primary key auto create id for every entry in dB
                                    choices=rvt_category_choice)        #inheritate the choices above class RvtFunctions
    rvt_level = models.CharField(max_length=50, choices=rvt_level_choice)
    job_category = models.CharField(max_length=50, choices=job_category_choice)
                                                                        # NOT utilized here: IntField does not have max_length - always check doc for more info
    ####### NEED FOREIGN KEY TO COMBINE BOTH dB #######

    RvtFunctions = models.Manager()                                     # use the models that we involked. Must be within the class.

    def __str__(self):                                                  # dunnder __str__: Django will use the result of the function to display objects of that type (in this case it will print self).
     return self.title                                                  # this take the object we entered & turn it into a string,
                                                                            # and return the title of the object. Always use the first object.

