from django.db import models
from datetime import datetime

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()
    event_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    event_date = models.DateField(default=datetime.now, blank=True)
    venue = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    event_l = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.title