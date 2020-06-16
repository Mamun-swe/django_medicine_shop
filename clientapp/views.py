from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    products = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    return render(request, "client/home.html", {'data': products})


def about(request):
    return render(request, "client/about.html")
