from django.contrib import admin

from .models import Person
from .models import ComparedPerson


admin.site.register(Person)
admin.site.register(ComparedPerson)
