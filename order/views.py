from IPython import embed
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from hq.models import ProductOrder
from hq.views import pay_for_cargo
from .models import Order
from product.models import Product
from .serializers import OrderSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def new_order(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data = data[0]
        billNo = pay_for_cargo(data['totalquantity'])
        order = Order.objects.create(totalquantity=data['totalquantity'], totalprice = data['totalprice'],
                             userid = data['userid'], trackNo = 0, billNo = billNo,
                             customerAddress = data['customerAddress'], customerPhone = data['customerPhone'])

        product_dict = data['products']
        for key in product_dict:
            ProductOrder.objects.create(pro_id=Product.objects.get(pk=key['id']), ord_id=Order.objects.get(pk=order.pk), quantity=key['quantity'])
        
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data, safe= False)

def list_order(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data, safe=False)