from django.contrib import admin
from . import models

@admin.register(models.Carbon_footprint)
class CarbonFootprintAdmin(admin.ModelAdmin):
    readonly_fields = ('kwh', 'carbon')

@admin.register(models.Usage)
class UsageAdmin(admin.ModelAdmin):
    pass