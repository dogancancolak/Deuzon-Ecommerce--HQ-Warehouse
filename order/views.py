from IPython import embed
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from hq.models import ProductOrder
from hq.views import pay_for_cargo, send_cargo
from .models import Order
from product.models import Product
from .serializers import OrderSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def new_order(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        data = data[0]
        product_dict = data['products']

        billNo = pay_for_cargo(data['totalquantity'])
        trackNo = send_cargo(billNo,data['customerAddress'],data['customerPhone'],data['products'])
        
        order = Order.objects.create(totalquantity=data['totalquantity'], totalprice = data['totalprice'],
                             userid = data['userid'], trackNo = trackNo, billNo = billNo,
                             customerAddress = data['customerAddress'], customerPhone = data['customerPhone'])
                             
        for key in product_dict:
            ProductOrder.objects.create(pro_id=Product.objects.get(pk=key['id']), ord_id=Order.objects.get(pk=order.pk), quantity=key['quantity'])
        
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data, safe= False)

def list_order(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)