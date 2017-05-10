from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^handle_product/$', views.handle_product, name='handle_product'),
    url(r'^$', views.index, name='index'),
]
