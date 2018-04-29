"""LoginReg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_register/?$', views.process_register),
    url(r'^process_login/?$', views.process_login),
    url(r'^dashboard', views.dashboard),
    url(r'^wish_list/(?P<item_id>\d+)$', views.wish_list),
    url(r'^create$', views.create),
    url(r'^createItem', views.createItem),
    url(r'addItem/(?P<item_id>\d+)$', views.addItem),
    url(r'removeItem/(?P<item_id>\d+)$', views.removeItem),
    url(r'deleteItem/(?P<item_id>\d+)$', views.deleteItem),
]
