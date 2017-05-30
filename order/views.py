from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from hq.models import ProductOrder
from hq.views import pay_for_cargo
from product.models import Product
from .models import Order
from .serializers import OrderSerializer


@csrf_exempt
def new_order(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        data = data[0]
        product_dict = data['products']
        for key in product_dict:
            pro = Product.objects.get(pk=key['id'])
            if pro.quantity < key['quantity']:
                return 403

        billNo = pay_for_cargo(data['totalQuantity'])
        # trackNo = send_cargo(billNo,data['address'],data['name'],data['surname'],data['totalQuantity'])

        order = Order.objects.create(totalquantity=data['totalQuantity'], totalprice=data['totalPrice'],
                                     userid=data['userid'], trackNo="0", billNo=billNo, customerAddress=data['address'],
                                     customerName=data['name'], customerSurname=data['surname'])

        for key in product_dict:
            ProductOrder.objects.create(pro_id=Product.objects.get(pk=key['id']), ord_id=Order.objects.get(pk=order.pk),
                                        quantity=key['quantity'])
            quant = Product.objects.get(pk=key['id']).quantity
            sold = Product.objects.get(pk=key['id']).soldcount
            Product.objects.filter(pk=key['id']).update(quantity=quant - key['quantity'],
                                                        soldcount=sold + key['quantity'])

        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data, safe=False)


def list_order(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)
