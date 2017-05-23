from django.db import models
from product.models import Product
from order.models import Order

# Create your models here.


class ProductOrder(models.Model):

    pro_id = models.ForeignKey(Product, related_name='ordered')
    ord_id = models.ForeignKey(Order, related_name='products')
    quantity = models.IntegerField(default=0, null=True)


class CargoPrice(models.Model):

    name = models.CharField(max_length=3,default="N", null=True)
    quantity = models.FloatField(default=0, null=True)
    price = models.PositiveIntegerField(default=0, null=True)
