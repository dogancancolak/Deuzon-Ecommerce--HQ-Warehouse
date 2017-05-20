from django.shortcuts import render
from .models import User
from hq.views import index
from authentication.views import login

# Create your views here.

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
