from django.contrib import admin


# Register your models here.
from .models import Character,Comment

admin.site.register(Character)
admin.site.register(Comment)
