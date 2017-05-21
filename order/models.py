from django.db import models

# Create your models here.

class Order(models.Model):

    order_id = models.AutoField(primary_key=True)
    totalquantity = models.IntegerField(default=0, null=True)
    totalprice = models.IntegerField(default=0, null=True)
    userid = models.IntegerField(default=0, null=True)
    trackNo = models.IntegerField(default=0, null=True)
    billNo = models.IntegerField(default=0, null=True)
    customerAddress = models.CharField(max_length=30,default="nil", null=True)
    customerPhone = models.CharField(max_length=30,default="nil", null=True)

    def __str__(self):
        line = str(self.order_id) + ' Userid : ' + str(self.userid)
        return line