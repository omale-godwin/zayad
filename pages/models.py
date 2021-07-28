from django.db import models

# Create your models here.
class Galary(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    galary = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return str(self.galary)
