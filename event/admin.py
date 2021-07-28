
from django.contrib import admin
from django.db import models
from django.db.models.base import Model
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'event_date', 'description', 'start_time', 'end_time')
    list_display = ('id', 'title', 'event_date')
    list_filter = ('title', 'event_date')
    list_per_page = 10

admin.site.register(Event, EventAdmin)