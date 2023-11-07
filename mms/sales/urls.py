#  -*- coding:utf-8 -*-
# @Time   :  2023.11
# @Author :  秦资鸿
# @Note   :
from django.urls import path
from . import views

urlpatterns = [
    path("order/" , views.listorders),
]