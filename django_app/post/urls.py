from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<post_pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^(?P<post_pk>\d+)/modify/$', views.post_modify, name='post_modify'),
    url(r'^post_create/$', views.post_create, name='post_create')
]