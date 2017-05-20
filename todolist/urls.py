from django.conf.urls import url
from . import views

app_name = 'todolist'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.CreateTodolist.as_view(), name='create_todolist'),
    url(r'^(?P<list_id>[0-9]+)/$', views.ListDetail.as_view(), name='list-detail'),
]

