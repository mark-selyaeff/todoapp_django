from django import forms

class TodolistCreateForm(forms.Form):
    name = forms.CharField(label='Todo list\'s name', max_length=50) # добавить кавычку после list's
