from django.contrib import admin

# Register your models here.
from .models import Causes

class CausesAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'total', 'description', 'current')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'total', 'current')


admin.site.register(Causes, CausesAdmin)