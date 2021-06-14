from django.contrib import admin

from petstagram.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'type', 'age']
    list_filter = ['type']


admin.site.register(Pet, PetAdmin)
