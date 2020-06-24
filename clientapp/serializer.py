from rest_framework import serializers
from .models import Users
from .models import Orders

class UsersSerialize(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'email', 'role')


class OrderSerialize (serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('name', 'email', 'phone', 'division', 'address', 'state', 'order_status')