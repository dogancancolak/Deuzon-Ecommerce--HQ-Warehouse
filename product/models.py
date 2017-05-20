from django.db import models

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=30,default="nil", null=True)
    author = models.CharField(max_length=30,default="nil", null=True)
    date = models.DateField(null=True)
    price = models.FloatField(default=0, null=True)
    quantity = models.IntegerField(default=0, null=True)
    soldcount = models.IntegerField(default=0, null=True)
    category = models.CharField(max_length=30,default="nil", null=True)