from django.contrib import admin
from pet.models import Pet


class PetAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('name', 'breed', 'slug', 'owner', 'created', 'modified')


admin.site.register(Pet, PetAdmin)
