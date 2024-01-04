from django.contrib import admin

from content.models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
