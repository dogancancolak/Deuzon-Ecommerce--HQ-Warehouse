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


class ProductOrder(models.Model):

    pro_id = models.IntegerField(default=0, null=True)
    ord_id = models.IntegerField(default=0, null=True)
    quantity = models.IntegerField(default=0, null=True)


class Order(models.Model):

    quantity = models.IntegerField(default=0, null=True)
    userid = models.IntegerField(default=0, null=True)
    trackNo = models.IntegerField(default=0, null=True)
    billNo = models.IntegerField(default=0, null=True)
    customerAddress = models.CharField(max_length=30,default="nil", null=True)
    customerPhone = models.CharField(max_length=30,default="nil", null=True)


class CargoPrice(models.Model):

    quantity = models.FloatField(default=0, null=True)
    price = models.PositiveIntegerField(default=0, null=True)
