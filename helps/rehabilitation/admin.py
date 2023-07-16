from django.contrib import admin

from helps.rehabilitation.models import RehabilitationCenter


@admin.register(RehabilitationCenter)
class RehabilitationCenterAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "address", "city", "website")
    filter_horizontal = ["inclusions"]
