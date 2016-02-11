#-*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from snippets import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]