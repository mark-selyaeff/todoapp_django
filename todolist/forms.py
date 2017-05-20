from django import forms

class TodolistCreateForm(forms.Form):
    name = forms.CharField(label='Todo list\'s name', max_length=50) # добавить кавычку после list's

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

