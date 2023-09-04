from django import forms
from .models import User

# Básicamente só existem dois tipos de formulários em django.

# 1- modelForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'telefone', 'email']

# 2- form.Form