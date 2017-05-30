import requests
from IPython import embed
from django.shortcuts import render

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
    data = {'source_account': 'TRDOGANCAN22', 'destination_account': 'TRMERTCAN22',
            'description': 'payment for ' + str(quantity) + ' cargo', 'password': '12345'}
    price = 0
    prices = CargoPrice.objects.all().order_by('-quantity')
    for element in prices:
        if element.quantity >= quantity:
            price = element.price
        else:
            break
    if price == 0:
        price = prices[0].price
    data['amount'] = int(price)
    r = requests.post('http://146.185.147.162/accounts/transaction/api/', data)
    r = r.json()
    return r['bank_receiptID']


def send_cargo(billNo, address, name, surname):
    data = {'billNo': billNo, 'Destaddress': address,
            'CompanyName': 'Deuzon E-Commerce', 'destname': name, 'destsurname': surname}
    trackNo = requests.post('cargo api', data)
    return trackNo
