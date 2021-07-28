from django.contrib import admin
from .models import Galary
# Register your models here.

class GalaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'galary')
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    list_per_page = 20

admin.site.register(Galary, GalaryAdmin)
