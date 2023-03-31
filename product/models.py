from django.db import models
#this is where you define class


class Product(models.Model):
    name = models.CharField(max_length=255) #charfield = contains textual data
    price = models.FloatField() #FloatField = contains floating point number
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
