from django.http import HttpResponse
from .models import Product
from authentication.models import User
from django.shortcuts import render
from IPython import embed

# Create your views here.


def index(request):

    products = Product.objects.all()
    users = User.objects.all()
    return render(request, 'index.html', {'products': products, 'users': users})


def createProduct(request):
    params = request.POST

    if (params["name"] is not "") and (params["author"] is not "") and (params["date"] is not "") and (params["price"] is not "") and (params["quantity"] is not "") and (params["soldcount"] is not "") and (params["category"] is not ""):
        embed()
        Product.objects.create(name=params["name"],
                               author=params["author"],
                               date=params["date"],
                               price=float(params["price"]),
                               quantity=params["quantity"],
                               soldcount=params["soldcount"],
                               category=params["category"])
        return index(request)
    else:
        return HttpResponse("asd")