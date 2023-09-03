from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    model = PlacesImage


@ admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [
        ImageInline,
    ]


@ admin.register(PlacesImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'place')
