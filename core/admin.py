from django.contrib import admin

from core.models import City, InclusionTag


@admin.register(City, InclusionTag)
class CoreAdmin(admin.ModelAdmin):
    pass
