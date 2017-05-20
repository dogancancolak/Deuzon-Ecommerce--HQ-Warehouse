from django.db import models

# Create your models here.


class ProductOrder(models.Model):

    pro_id = models.IntegerField(default=0, null=True)
    ord_id = models.IntegerField(default=0, null=True)
    quantity = models.IntegerField(default=0, null=True)


class CargoPrice(models.Model):

    quantity = models.FloatField(default=0, null=True)
    price = models.PositiveIntegerField(default=0, null=True)
