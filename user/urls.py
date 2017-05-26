from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/(?P<id>\w+)/$', views.create_user),
    url(r'^create/$', views.create_user),
    url(r'^del/(\d+)/', views.delete_user, name = 'delete_user'),
    url(r'^$', views.user_list, name='user_list'),
]