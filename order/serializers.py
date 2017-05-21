from rest_framework import serializers
from .models import Order
from hq.models import ProductOrder


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = ('order_id', 'totalquantity', 'totalprice', 'userid', 'customerAddress', 'customerPhone', 'trackNo', 'products')


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ('pro_id', 'ord_id', 'quantity')
