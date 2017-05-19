from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic, View
import requests
from django.http import HttpResponseRedirect
from .forms import TodolistCreateForm, LoginForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.

def index(request):
    r = requests.get('http://127.0.0.1:8080/todolists/')
    todolists = r.json()
    return render(request, 'index.html', {'todolists': todolists})

class CreateTodolist(View):
    def get(self, request, *args, **kwargs):
        form = TodolistCreateForm()
        return render(request, 'create_todolist.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TodolistCreateForm(request.POST)
        if form.is_valid():
            post_data = {'name': form.cleaned_data['name']}
            response = requests.post('http://127.0.0.1:8080/todolists/', data=post_data)
            return HttpResponseRedirect('/todolists/')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    def post(self, request, *args, **kwargs):
        # token = django.middleware.csrf.get_token(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            r = requests.get('http://127.0.0.1:8080/api-auth/login/')

            post_data = {'username': form.cleaned_data['username'], 'password': form.cleaned_data['password']}
            response = requests.post('http://127.0.0.1:8080/api-auth/login/', data=post_data)
            return HttpResponseRedirect('/todolists/')

