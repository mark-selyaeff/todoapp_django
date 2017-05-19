from django.conf.urls import url
from . import views

app_name = 'todolist'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.CreateTodolist.as_view(), name='create_todolist'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
]

