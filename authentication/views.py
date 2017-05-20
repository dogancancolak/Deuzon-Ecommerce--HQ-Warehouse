from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
from hq.views import index


# Create your views here.


def makeAuth(request):
    if User.objects.filter(username=request.POST["username"], password=request.POST["password"]):
        return index(request)
    else:
        return HttpResponse("403")


def register(request):
    return render(request, 'templates/register.html', {})


def login(request):
    return render(request, 'templates/login.html', {})


