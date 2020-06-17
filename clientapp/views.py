from django.shortcuts import render, HttpResponse
from .models import Users
from .forms import UsersForms

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


def register_form_submission(request):
    form = UsersForms(request.POST or None)
    if form.is_valid():
        form.save()

    response = {
        'message': 'Successfully account created'
    }

    print(response)

    return render(request, "auth/register.html", {'response': response})
    # if request.method == 'POST':
    #     name = request.POST["name"]
    #     email = request.POST["email"]
    #     password = request.POST["password"]

    #     print(name, email, password)
    #     return render(request, "auth/register.html")
    # else:
    #     return render(request, "auth/register.html")


def reset(request):
    return render(request, "auth/reset.html")
