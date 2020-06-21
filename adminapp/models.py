from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=250, unique=True)
    price = models.IntegerField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    product_images = models.FileField(upload_to='product_images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
