from django.shortcuts import render, HttpResponse

# Create your views here.

def dashboard(request):
    return render(request, "admin/dashboard.html")