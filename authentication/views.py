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
    return render(request, 'register.html', {})


def login(request):
    return render(request, 'login.html', {})


def create_user(request):
    params = request.POST

    if (params["email"] is not "") \
            and (params["username"] is not "") \
            and (params["password"] is not "") \
            and (params["passwordagain"] == params["password"]):
        User.objects.update_or_create(email=params["email"],
                                      defaults={"username": params["username"],
                                                "password": params["password"],
                                                "isAdmin": params["isadmin"]}
                                      )

    if params["homepage"] == "1":
        return index(request)
    else:
        return login(request)


def delete_user(request):
    params = request.POST

    if (params["username"] is not "") \
            and (params["email"] is not "") \
            and (params["password"] is not ""):
        user = User.objects.get(username=params["username"],
                                      password=params["password"],
                                      email=params["email"]).pk

        User.objects.filter(pk=user).delete()
    return index(request)


def handle_user(request):
    if request.POST["button"] == "create":
        return create_user(request)
    elif request.POST["button"] == "delete":
        return delete_user(request)
