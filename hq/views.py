from django.http import HttpResponse
from .models import Product
from user.models import User
from django.shortcuts import render

# Create your views here.


def index(request):

    products = Product.objects.all()
    users = User.objects.all()
    return render(request, 'index.html', {'products': products, 'users': users})


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
            and (params["author"] is not "") \
            and (params["date"] is not "") \
            and (params["price"] is not "") \
            and (params["quantity"] is not "") \
            and (params["soldcount"] is not "") \
            and (params["category"] is not ""):
        product = Product.objects.get(name=params["name"],
                                      author=params["author"],
                                      date=params["date"],
                                      price= float(params["price"]),
                                      quantity= params["quantity"],
                                      soldcount= params["soldcount"],
                                      category= params["category"]).pk

        Product.objects.filter(pk=product).delete()
    return index(request)


def handle_product(request):
    if request.POST["button"] == "create":
        return create_product(request)
    elif request.POST["button"] == "delete":
        return delete_product(request)
