#-*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username', 'first_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','maxlength':255}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 255}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255}),
        }

        erros_messages = {
            'first_name': {'required': 'Este campo é obrigatório'},
            'username': {'required': 'Este campo é obrigatório'},
            'email': {'required': 'Escreva um Email válido'},
            'password': {'required': 'Este campo é obrigatório'},

        }
