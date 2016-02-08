from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class StepCount(models.Model):
    owner = models.ForeignKey(User)
    dateCreated = models.DateTimeField(auto_now_add=True)

