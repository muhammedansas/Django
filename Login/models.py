from django.db import models

# Create your models here.

class Dummyitems(models.Model):
    name = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    description = models.TextField()
    