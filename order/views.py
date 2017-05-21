from IPython import embed
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from hq.models import ProductOrder
from .models import Order
from .serializers import OrderSerializer
# Create your views here.

def new_order(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        order = Order.objects.create(totalquantity=data['totalquantity'], totalprice = data['totalprice'],
                             userid = data['userid'], trackno = 0, billno = 0,
                             customerAddress = data['customerAddress'], customerPhone = data['customerPhone'])

        product_dict = data['products']
        for key in product_dict:
            ProductOrder.objects.create(pro_id=key, ord_id=order.pk, quantity=product_dict[key])

def list_order(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)