from django.http import HttpResponse
from .models import Product, User
from django.shortcuts import render

# Create your views here.


def index(request):

    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def login(request):

    return render(request, 'login.html', {})


def makeAuth(request):

    theUser = User.objects.filter(username=request.POST["username"],password=request.POST["password"])
    if theUser:
        return index(request)
    else:
        return HttpResponse("boş")