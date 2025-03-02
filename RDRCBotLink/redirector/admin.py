from django.contrib import admin

from .models import LinkBase
@admin.register(LinkBase)
class LinkBase(admin.ModelAdmin):
    list_display  = ['name',]


