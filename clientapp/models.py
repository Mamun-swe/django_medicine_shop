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
