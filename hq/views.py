import requests
from django.shortcuts import render

from IPython import embed
from product.models import Product
from user.models import User
from .models import CargoPrice


def index(request, selected=0, selectedUser=0):
    if selected:
        products = Product.objects.all()
        users = User.objects.all()
        return render(request, 'index.html', {'products': products, 'users': users, 'selected': selected})
    elif selectedUser:
        products = Product.objects.all()
        users = User.objects.all()
        return render(request, 'index.html', {'products': products, 'users': users, 'selectedUser': selectedUser})
    else:
        products = Product.objects.all()
        users = User.objects.all()
        return render(request, 'index.html', {'products': products, 'users': users})


def get_cargo_prices():
    response = requests.get('cargos web api')
    response = response.json()
    for key in response:
        CargoPrice.objects.Create(name=key['name'], quantity=key['count'], price=key['price'])


def pay_for_cargo(quantity):
    data = {'IBAN': 'cargo_company_IBAN'}
    price = 0
    prices = CargoPrice.objects.all().order_by('-quantity')
    for element in prices:
        if element.quantity >= quantity:
            price = element.price
        else:
            break
    data['price'] = price
    r = requests.post('bank api', data)
    return r


def send_cargo(billNo, phone, address, sourceAddress, name, surname):
    data = {'billNo': billNo, 'phone': phone, 'Destaddress': address, 'SourceAddress': sourceAddress,
            'CompanyName': 'Deuzon E-Commerce', 'destname': name, 'destsurname': surname}
    trackNo = requests.post('cargo api', data)
    return trackNo
