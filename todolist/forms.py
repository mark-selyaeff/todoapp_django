from django import forms
from todolist.models import User
import datetime

class TodolistCreateForm(forms.Form):
    name = forms.CharField(label='Todo list\'s name', max_length=50) # добавить кавычку после list's

class TodolistUpdateForm(forms.Form):
    name = forms.CharField(label='Todo list\'s name', max_length=50)

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class TaskCreateForm(forms.Form):
    name = forms.CharField(label = 'Task name', max_length=50)
    description = forms.CharField(widget=forms.Textarea, max_length=1000, label='Description')
    completed = forms.BooleanField()
    date_created = forms.DateField(initial=datetime.date.today)
    due_date = forms.DateField()
    date_created = forms.DateField(initial=datetime.date.today)
    tags = forms.CharField(label = "Tags", max_length=100)