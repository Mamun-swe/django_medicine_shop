from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('register_form_submission/', views.registration_submission, name="registration_submission"),
    path('reset/', views.reset, name="reset"),
    path('users', views.all_register_users, name="users"),
]
