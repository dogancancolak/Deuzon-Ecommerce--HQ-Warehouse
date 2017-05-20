from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^handle_user/$', views.handle_user, name='handle_user'),
    url(r'^$', views.user_list, name='user_list'),
]