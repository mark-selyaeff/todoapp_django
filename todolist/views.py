from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic, View
import requests
from django.http import HttpResponseRedirect
from .forms import TodolistCreateForm, LoginForm
# Create your views here.

def index(request):
    token = request.session.get('token', False)
    headers = {'Authorization': 'Token {}'.format(token if token else '')}
    r = requests.get('http://127.0.0.1:8080/todolists/', headers=headers)
    todolists = r.json()
    # request.session.flush()
    return render(request, 'index.html', {'todolists': todolists, 'session': request.session})

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
        form = LoginForm(request.POST)
        if form.is_valid():
            post_data = {'username': form.cleaned_data['username'], 'password': form.cleaned_data['password']}
            response = requests.post('http://127.0.0.1:8080/api-token-auth/', data=post_data)
            credentials = response.json()
            if credentials.get('token', False):
                request.session['token'] = credentials['token']
                print('token in session')
                print(request.session['token'])
                return HttpResponseRedirect("/todolists/")
            else:
                print('not found token')
                return HttpResponse("You email/password is wrong!", status=403)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        request.session.flush()
        return HttpResponseRedirect('/todolists/')