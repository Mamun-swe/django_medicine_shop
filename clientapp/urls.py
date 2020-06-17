from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('/about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('register_form_submission/', views.register_form_submission, name="register_form_submission"),
    path('reset/', views.reset, name="reset"),
]
