from product.models import Product
from user.models import User
from django.shortcuts import render
from django.shortcuts import render


# Create your views here.


def index(request):

    products = Product.objects.all()
    users = User.objects.all()
    return render(request, 'index.html', {'products': products, 'users': users})



