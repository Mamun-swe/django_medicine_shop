from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users
from adminapp.models import Products
from .serializer import UsersSerialize
from adminapp.serializer import ProductSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def home(request):
    allproducts = Products.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(allproducts, 20)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "client/home.html", {'product': products})


@api_view(['GET'])
def productView(request, id):
    try:
        list = Products.objects.get(id=id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProductSerializer(list)
        return Response(serializer.data)


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
