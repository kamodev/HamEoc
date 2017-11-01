from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ['name']


# Register the admin for URL resolve
admin.site.register(Location, LocationAdmin)
