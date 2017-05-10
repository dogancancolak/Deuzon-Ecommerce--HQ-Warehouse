from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^makeAuth/$', views.makeAuth, name='makeAuth'),
    url(r'^createUser/$', views.createUser, name='createUser'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register')
]
