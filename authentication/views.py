from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from hq.views import index
from IPython import embed

# Create your views here.


def makeAuth(request):

    if User.objects.filter(username=request.POST["username"], password=request.POST["password"]):
        return index(request)
    else:
        return HttpResponse("403")


def register(request):

    return render(request, 'register.html',{})


def login(request):

    return render(request, 'login.html', {})


def createUser(request):
    params = request.POST
    embed()
    if (params["email"] is not "") \
            and (params["username"] is not "") \
            and (params["password"] is not "") \
            and (params["passwordagain"] == params["password"]):

        User.objects.create(email=params["email"],
                               username=params["username"],
                               password=params["password"],
                               isAdmin=bool(params["isadmin"]))
        return login(request)
    else:
        return HttpResponse("asd")
