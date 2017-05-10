from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^createProduct/$', views.createProduct, name='createProduct'),
    url(r'^$', views.index, name='index'),
]
