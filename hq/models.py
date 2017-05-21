from django.db import models
from product.models import Product
from order.models import Order

# Create your models here.


class ProductOrder(models.Model):

    pro_id = models.IntegerField(default=0,null=True)
    ord_id = models.ForeignKey(Order, related_name='products')
    quantity = models.IntegerField(default=0, null=True)

    def __str__(self):
        return (Product.objects.get(pk=self.pro_id).name) + " : " + str(self.quantity)


class CargoPrice(models.Model):

    quantity = models.FloatField(default=0, null=True)
    price = models.PositiveIntegerField(default=0, null=True)
