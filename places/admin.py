from django.contrib import admin
from .models import *
from django.utils.html import format_html, mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase


@ admin.register(PlacesImage)
class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('position',
                    'place')


class ImageInline(SortableTabularInline):
    model = PlacesImage
    fields = ('image',
              'get_preview',
              'position')

    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return format_html('<img src="{url}" height=200 />', url=mark_safe(obj.image.url))


@ admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [
        ImageInline,
    ]




