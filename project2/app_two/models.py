from django.db import models

# Create your models here.
class student(models.Model):
     name = models.CharField(max_length=126)
     age = models.IntegerField(max_length=3)
     gender = models.BooleanField(default=True) # True = male , False = female 
     photo = models.ImageField(upload_to='images')
     mobile = models.CharField(max_length=10)
    
# name , salary , post  , gender , image , description 

class employee(models.Model):
     name = models.CharField(max_length=56)
     salary = models.IntegerField()
     post = models.CharField(max_length=56)
     gender = models.BooleanField(default=True)
     image = models.ImageField(upload_to='images')
     description = models.TextField()