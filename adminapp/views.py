from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .serializer import ProductSerializer
# Create your views here.


def dashboard(request):
    return render(request, "admin/dashboard.html")


def productIndex(request):
    products = Products.objects.all()
    return render(request, "admin/product/index.html", {'product': products})


def productCreate(request):
    return render(request, "admin/product/create.html")


def productEdit(request, id):
    try:
        return render(request, "admin/product/edit.html")
    except Products.DoesNotExist:
        return render(request, "admin/product/index.html")


def productView(request, id):
    try:
        return render(request, "admin/product/view.html")
    except Products.DoesNotExist:
        return render(request, "admin/product/index.html")


# Product API's
@api_view(['GET', 'POST'])
def product(request):
    if request.method == 'GET':
        list = Products.objects.all()
        serializer = ProductSerializer(list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def productShow(request, id):
    try:
        list = Products.objects.get(id=id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProductSerializer(list)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = "success"
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
