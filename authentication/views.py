from django.http import HttpResponse
from django.shortcuts import render

from hq.views import index
from user.models import User


# Create your views here.


def makeAuth(request):
    usr = User.objects.filter(username=request.POST["username"], password=request.POST["password"])
    if usr:
        return index(request)
    else:
        return HttpResponse("403")


def register(request):
    return render(request, 'register.html', {})


def login(request):
    return render(request, 'login.html', {})
