from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from hq.views import index
from .models import Product
from .serializers import ProductSerializer


# Create your views here.

def create_product(request, id=''):
    params = request.POST

    if id != "" or params['id'] != "":

        Product.objects.update_or_create(pk=params["id"],
                                         defaults={
                                             "name": params["name"],
                                             "author": params["author"],
                                             "date": params["date"],
                                             "price": params["price"],
                                             "quantity": params["quantity"],
                                             "soldcount": params["soldcount"],
                                             "category": params["category"]
                                         })
        return index(request)
    else:
        if (params["name"] is not "") \
                and (params["author"] is not "") \
                and (params["date"] is not "") \
                and (params["price"] is not "") \
                and (params["quantity"] is not "") \
                and (params["soldcount"] is not "") \
                and (params["category"] is not ""):
            Product.objects.create(name=params["name"],
                                   author=params["author"],
                                   date=params["date"],
                                   price=float(params["price"]),
                                   quantity=params["quantity"],
                                   soldcount=params["soldcount"],
                                   category=params["category"])
        return index(request)


def delete_product(request, id):
    Product.objects.filter(pk=id).delete()
    return index(request)


def edit_product(request, id):
    selected = Product.objects.get(pk=id)
    return index(request, selected)


@csrf_exempt
def product_list(request):

    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
