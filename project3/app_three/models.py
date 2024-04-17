from django.db import models

# Create your models here.
class category(models.Model):
     name = models.CharField(max_length=24)
     description = models.TextField()
     photo = models.ImageField(upload_to='images')
     total = models.IntegerField()