from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=25000)
class Offer(models.Model):
    name=models.CharField(max_length=255)
    discount=models.FloatField()
    image=models.CharField(max_length=25000)
