from IPython import embed
from .models import Product
from hq.views import index
from .serializers import ProductSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

# Create your views here.

def create_product(request):
    params = request.POST

    if (params["name"] is not "") \
            and (params["author"] is not "") \
            and (params["date"] is not "") \
            and (params["price"] is not "") \
            and (params["quantity"] is not "") \
            and (params["soldcount"] is not "") \
            and (params["category"] is not ""):

        Product.objects.update_or_create(name=params["name"],
                                            author=params["author"],
                                            date=params["date"],
                                         defaults={
                                            "price":float(params["price"]),
                                            "quantity":params["quantity"],
                                            "soldcount":params["soldcount"],
                                            "category":params["category"]})
    return index(request)


def delete_product(request):
    params = request.POST

    if (params["name"] is not "") \
            and (params["author"] is not ""):
        product = Product.objects.get(name=params["name"],
                                      author=params["author"]).pk

        Product.objects.filter(pk=product).delete()
    return index(request)



@csrf_exempt
def product_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        embed()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        embed()
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def handle_product(request):
    if request.POST["button"] == "create":
        return create_product(request)
    elif request.POST["button"] == "delete":
        return delete_product(request)