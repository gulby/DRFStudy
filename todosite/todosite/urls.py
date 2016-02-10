#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

"""todosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
#from todo import views

urlpatterns = [
    #url(r'^register/$', views.RegistrationView.as_view()),
    #url(r'^todos/$', views.TodosView.as_view()),
    #url(r'^todos/(?P<todo_id>\d+)/$', views.TodosView.as_view()),
    
    #url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', admin.site.urls),
]
