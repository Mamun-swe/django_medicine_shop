from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(unique=True, max_length=250)
    role = models.CharField(max_length=100)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Orders(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=150)
    division = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    order_status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
