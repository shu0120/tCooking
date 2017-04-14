from django.conf.urls import  include, url
from . import views


urlpatterns = [
    url(r'^$', views.formulate_list, name='formulate_list'),
    url(r'^formulate/(?P<pk>[0-9]+)/$', views.formulate_detail, name='formulate_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit')
]
