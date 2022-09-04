from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Provider

@admin.register(Provider)
class ProviderAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'contact', 'provider_type')
