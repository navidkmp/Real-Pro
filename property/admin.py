from django.contrib import admin
from property.models import Agent
from .models import Property, Owner, PropertyImage


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'whatsapp')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'house_name',
        'location',
        'price',
        'bedrooms',
        'bathrooms',
        'year_built',
        'owner',
    )
    prepopulated_fields = {
        'slug': ('house_name',)
    }


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property',)


admin.site.register(Agent)
