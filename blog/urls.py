# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 22:47:37 2018

@author: SANTIAGO
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
