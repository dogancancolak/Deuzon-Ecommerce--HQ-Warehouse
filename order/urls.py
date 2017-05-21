from django.conf.urls import url

from .views import list_order

urlpatterns = [
    url(r'^$', list_order, name='list_order')
]