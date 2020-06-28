from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('product/<int:id>/view', views.productView, name="product-view"),
    path('cart/', views.cart),
    path('checkout/', views.checkout),
    path('order/place/', views.placeOrder),

    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
 
    path('reset/', views.reset, name="reset"),
]
