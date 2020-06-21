from rest_framework import serializers
from .models import Users

class UsersSerialize(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'email', 'role')
