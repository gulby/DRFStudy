#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.db import models
from django.contrib.auth.models import User
#User = get_user_model()


class Todo(models.Model):
    owner = models.ForeignKey(User)
    description = models.CharField(max_length=30)
    done = models.BooleanField()
    updated = models.DateTimeField(auto_now_add=True)
    