# -*- coding: UTF-8 -*-     
# @IDE      ：PyCharm
# @Author   ：guduyao
# @Date     ：2021/8/11 12:21
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]