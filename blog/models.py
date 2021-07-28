from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    blog_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    blog_date = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title