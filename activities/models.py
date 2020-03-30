from django.db import models
import datetime

# Create your models here.
class Technical(models.Model):
    title = models.CharField(max_length=255, unique=True)
    branch = models.CharField(max_length=255, default = "")
    backGroundPhoto = models.ImageField(upload_to='backGround/', height_field=None, width_field=None, max_length=100)
    littleSummary = models.TextField()
    smallDescription = models.TextField()
    longDescription = models.TextField()
    firstPhoto = models.ImageField(upload_to='first/', height_field=None, width_field=None, max_length=100)
    secondPhoto = models.ImageField(upload_to='second/', height_field=None, width_field=None, max_length=100)
    date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.title

class Social(models.Model):
    title = models.CharField(max_length=255, unique=True)
    branch = models.CharField(max_length=255, default = "")
    backGroundPhoto = models.ImageField(upload_to='backGround/', height_field=None, width_field=None, max_length=100)
    littleSummary = models.TextField()
    smallDescription = models.TextField()
    longDescription = models.TextField()
    firstPhoto = models.ImageField(upload_to='first/', height_field=None, width_field=None, max_length=100)
    secondPhoto = models.ImageField(upload_to='second/', height_field=None, width_field=None, max_length=100)
    date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.title