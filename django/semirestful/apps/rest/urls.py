from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addpage$', views.addpage),
    url(r'^adduser$', views.adduser),
    url(r'^show/(?P<id>\d+)$',views.show),
    url(r'^delete/(?P<id>\d+)$',views.deleteuser),
    url(r'^edit/(?P<id>\d+)$',views.edit),
    url(r'^edituser/(?P<id>\d+)$',views.edituser)
]