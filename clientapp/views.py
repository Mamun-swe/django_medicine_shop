from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users
from .serializer import UsersSerialize


# Create your views here.


def home(request):
    products = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    return render(request, "client/home.html", {'data': products})


def about(request):
    return render(request, "client/about.html")


def login(request):
    return render(request, "auth/login.html")


def register(request):
    return render(request, "auth/register.html")


def registration_submission(request):
    return render(request, "auth/register.html")


@api_view(['GET'])
def all_register_users(request):
    if request.method == "GET":
        list = Users.objects.all()
        serializer = UsersSerialize(list, many=True)
        return Response(serializer.data)


def reset(request):
    return render(request, "auth/reset.html")
