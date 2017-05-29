from .models import User
from hq.views import index
from authentication.views import login
from .serializers import UserSerializer
from django.http import JsonResponse
from django.http import JsonResponse

from authentication.views import login
from hq.views import index
from .models import User
from .serializers import UserSerializer


def create_user(request):
    params = request.POST
    if params['id'] != "":
        User.objects.update_or_create(pk=params["id"],
                                      defaults={
                                          "username": params["username"],
                                          "password": params["password"],
                                          "isAdmin": params["isAdmin"],
                                          "email": params["email"],
                                      })
        return index(request)
    else:
        if (params["email"] is not "") \
                and (params["username"] is not "") \
                and (params["password"] is not ""):
            User.objects.create(email=params["email"],
                                username=params["username"],
                                password=params["password"],
                                isAdmin=params["isAdmin"]
                                )

        if params["homepage"] == "1":
            return index(request)
        else:
            return login(request)


def delete_user(request, id):
    User.objects.filter(pk=id).delete()
    return index(request)


def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)


def edit_user(request, id):
    selectedUser = User.objects.get(pk=id)
    return index(request, selectedUser=selectedUser)
