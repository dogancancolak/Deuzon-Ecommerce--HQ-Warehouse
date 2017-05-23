from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_order, name='list_order'),
    url(r'^new/$', views.new_order, name='new_order')
]