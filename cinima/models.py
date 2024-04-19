from django.db import models

# Create your models here.

class Movies(models.Model):
    movie_name = models.CharField(max_length=250)
    movie_type = models.CharField(max_length=250)
    description = models.TextField()
    movie_image = models.ImageField(upload_to='cinima')