from product.models import Product
from user.models import User
from django.shortcuts import render
from .models import CargoPrices
import requests


# Create your views here.


def index(request):

    products = Product.objects.all()
    users = User.objects.all()
    return render(request, 'index.html', {'products': products, 'users': users})


def get_cargo_prices():
    response = requests.get('cargos web api')
    response = response.json()
    for key in response:
        CargoPrices.objects.Create(name=key['name'], quantity= key['count'], price= key['price'])


def pay_for_cargo(quantity):
    data = {'IBAN':'cargo_company_IBAN'}
    price = 0
    prices = CargoPrices.objects.all().order_by('-quantity')
    for element in prices :
        if element.quantity >= quantity:
            price = element.price
        else:
            break
    data['price'] = price
    r = request.post('bank api',data)
    return r


