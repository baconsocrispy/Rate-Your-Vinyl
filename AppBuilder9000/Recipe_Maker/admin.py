from django.contrib import admin

from .models import RecipeName, Ingredients, Description


# inlines allow models to be edited on the same page as the parent model
class IngredientsInline(admin.TabularInline):
    model = Ingredients
    extra = 5


class DescriptionInline(admin.TabularInline):
    model = Description


# add the inlines to the model
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientsInline,
        DescriptionInline,
    ]


admin.site.register(RecipeName, RecipeAdmin)
