from django import forms
from .models import Users


class UsersForms(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            'name',
            'email',
            'role',
            'password'
        ]
