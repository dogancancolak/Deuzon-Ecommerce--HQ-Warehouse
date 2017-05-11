from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^makeAuth/$', views.makeAuth, name='makeAuth'),
    url(r'^handle_user/$', views.handle_user, name='handle_user'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register')
]
