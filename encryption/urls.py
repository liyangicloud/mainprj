#coding=utf-8
#this urs is just for encryption app
__author__ = 'Leon'


from django.conf.urls import url
from encryption import views

urlpatterns = [
    url(r'^$', views.encryptionMain),
    url(r'^get/(\d+)/$',views.testGet)

]
