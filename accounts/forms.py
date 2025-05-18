from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class MinimalUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']