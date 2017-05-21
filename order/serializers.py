from rest_framework import serializers
from .models import Order


class ProductListingSerializer(serializers.RelatedField):

    def to_representation(self, value):
        dict={}
        dict['name'] = value.pro_id.name
        dict['id'] = value.pro_id.pk
        dict['quantity'] = value.quantity
        return dict


class OrderSerializer(serializers.ModelSerializer):
    products = ProductListingSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('order_id', 'totalquantity', 'totalprice', 'userid', 'customerAddress', 'customerPhone', 'trackNo', 'products')
