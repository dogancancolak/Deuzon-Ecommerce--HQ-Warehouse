from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/(?P<id>\w+)/$', views.create_product),
    url(r'^create/$', views.create_product),
    url(r'^del/(\d+)/', views.delete_product, name = 'delete_product'),
    url(r'^$', views.product_list, name='product_list'),
]
