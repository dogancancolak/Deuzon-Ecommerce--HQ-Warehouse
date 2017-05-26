from django.conf.urls import url

from . import views
from product import views as pviews
from user import views as uviews

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/(\d+)/$', pviews.edit_product),
    url(r'^user/(\d+)/$', uviews.edit_user),
]
