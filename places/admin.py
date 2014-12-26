from django.contrib import admin

from places.models import Place


class PlaceAdmin(admin.ModelAdmin):
    class Meta:
        model = Place


admin.site.register(Place, PlaceAdmin)
