from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    date = models.DateField
    price = models.PositiveIntegerField
    quantity = models.IntegerField
    soldcount = models.IntegerField
    category = models.CharField
    image = models.ImageField


class ProductOrder(models.Model):
    pro_id = models.IntegerField
    ord_id = models.IntegerField
    quantity = models.IntegerField


class Order(models.Model):
    quantity = models.IntegerField
    userid = models.IntegerField
    trackNo = models.IntegerField
    billNo = models.IntegerField
    customerAddress = models.CharField
    customerPhone = models.CharField
    

class User(models.Model):
    email = models.CharField
    username = models.CharField
    password = models.CharField


class CargoPrice(models.Model):
    quantity = models.IntegerField
    price = models.PositiveIntegerField
