from django.http import HttpResponse
from .models import Product, User
from django.shortcuts import render
from IPython import embed

# Create your views here.


def index(request):

    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def login(request):

    return render(request, 'login.html', {})


def makeAuth(request):

    theUser = User.objects.filter(username=request.POST["username"], password=request.POST["password"])
    if theUser:
        return index(request)
    else:
        return HttpResponse("403")


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