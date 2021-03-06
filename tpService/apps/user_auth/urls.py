#!/usr/bin/python
# -*- coding:utf-8 _*- 
"""
@author:TXU
@file:urls.py
@time:2021/11/27
@email:tao.xu2008@outlook.com
@description:
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MyTokenObtainPairView, LogoutAPIView, UserProfileViewSet


router = DefaultRouter()

router.register(r'user/info', UserProfileViewSet, basename='retrieve'),
router.register(r'user/list', UserProfileViewSet, basename='list'),
router.register(r'user/add', UserProfileViewSet, basename='create'),
router.register(r'user/update', UserProfileViewSet, basename='update'),
router.register(r'user/del', UserProfileViewSet, basename='destroy')


urlpatterns = [
    path('', include(router.urls)),
    path('user/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/logout', LogoutAPIView.as_view(), name='logout'),
]


if __name__ == '__main__':
    pass
