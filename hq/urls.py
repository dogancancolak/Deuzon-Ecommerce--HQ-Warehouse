from django.conf.urls import url

from . import views
from product import views as pviews

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/(\d+)/$', pviews.edit_product)
]
