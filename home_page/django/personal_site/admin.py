from django.contrib import admin
from .models import HomepageStream


@admin.register(HomepageStream)
class HomepageStreamAdmin(admin.ModelAdmin):
    list_display = ("stream", "column", "sort_order")
    list_editable = ("column", "sort_order")
    ordering = ("sort_order",)
