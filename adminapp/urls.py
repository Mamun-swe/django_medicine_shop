from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('product/index/', views.productIndex, name="product-index"),
    path('product/create/', views.productCreate, name="product-create"),
    path('product/<int:id>/edit/', views.productEdit, name="product-edit"),
    path('product/<int:id>/view/', views.productView, name="product-view"),
    
    path('product/', views.product, name="product"),
    path('product/<int:id>', views.productShow, name="product-show"),
]
