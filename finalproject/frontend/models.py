from django.db import models

# Create your models here.
class admin(models.Model):
     email = models.CharField(max_length=24)
     password = models.CharField(max_length=126)

class category(models.Model):
     name = models.CharField(max_length=56)
     image = models.ImageField(upload_to='images/')

class product(models.Model):
     name = models.CharField(max_length=56)
     image = models.ImageField(upload_to='images')
     price = models.IntegerField()
     categoryid = models.IntegerField()
     detail = models.TextField()
     product_code = models.CharField(max_length=56)

class user(models.Model):
     name = models.CharField(max_length=56)
     phone = models.CharField(max_length=10)
     email = models.CharField(max_length=56)
     password = models.CharField(max_length=126)
     age = models.IntegerField()

class cart(models.Model):
     userid = models.IntegerField()
     productid = models.IntegerField()
     price = models.IntegerField()
     quantity = models.IntegerField()
     orderid = models.IntegerField()

class orders(models.Model):
     userid = models.IntegerField()
     amount = models.IntegerField()
     address = models.TextField()
     city = models.CharField(max_length=56)
     state = models.CharField(max_length=56)
     description = models.TextField()
     mode_of_payment = models.IntegerField()