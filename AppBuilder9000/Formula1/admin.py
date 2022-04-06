from django.contrib import admin

# Register your models here.
from .models import Team, Race, Driver, Result

admin.site.register(Team)
admin.site.register(Race)
admin.site.register(Driver)
admin.site.register(Result)