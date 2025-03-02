from django.contrib import admin

from .models import LinkBase , utmBase
@admin.register(LinkBase)
class LinkBase(admin.ModelAdmin):
    list_display  = ['name',]

@admin.register(utmBase)
class utmBase(admin.ModelAdmin):
    list_display  = ['unicKye','utms',]


