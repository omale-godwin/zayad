from django.db import models
from datetime import datetime

# Create your models here.
class Causes(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    total = models.FloatField(blank=True, null=True)
    causes_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    current = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title